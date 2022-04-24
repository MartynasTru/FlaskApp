from datetime import timedelta
from urllib.parse import urlparse, urljoin

from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, login_required
from flask_login import logout_user
from sqlalchemy.exc import IntegrityError

from my_flask_app import login_manager
from my_flask_app.__init__ import db
from my_flask_app.auth.forms import SignupForm, LoginForm, ResetForm, AfterConfirmation
from my_flask_app.mail import send_email
from my_flask_app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/auth')
def auth():
    return "This is the authentication section of the web app"


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Hello, {user.first_name} {user.last_name}. You are signed up.")
        except IntegrityError:
            db.session.rollback()
            flash(f'Error, unable to register {form.email.data}. ', 'error')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        login_user(user, remember=login_form.remember.data, duration=timedelta(minutes=1))
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        return redirect(next or url_for('main.index'))
    return render_template('login.html', title='Login', form=login_form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth_bp.route('/pswreset', methods=['GET', 'POST'])
def pswreset():
    form = ResetForm()

    if request.method == 'GET':
        return render_template('pswreset.html', title='Reset', form=form)

    if request.method == 'POST':

        email = request.form.get('email')
        user = User.verify_email(email)

        if user:
            send_email(user)
            flash('Email has been sent')

        return redirect(url_for('auth.login'))


@auth_bp.route('/resetverified/<token>', methods=['GET', 'POST'])
def reset_verified(token):
    form = AfterConfirmation()
    user = User()
    userr = User.verify_reset_token(token)

    if not userr:
        flash('No user found ')
        return redirect(url_for('auth.signup'))

    password = request.form.get('password')
    if password:
        if form.password.data == form.password_repeat.data:
            user.set_password(form.password.data)
        else:
            flash("Passwords did not match, please try again")
            return redirect(url_for('auth.login'))

    return render_template('resetverified.html', user=user, token=token, form=form, _external=True)


@login_manager.user_loader
def load_user(user_id):
    """ Takes a user ID and returns a user object or None if the user does not exist"""
    if user_id is not None:
        return User.query.get(user_id)
    return None


def is_safe_url(target):
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return redirect_url.scheme in ('http', 'https') and host_url.netloc == redirect_url.netloc


def get_safe_redirect():
    url = request.args.get('next')
    if url and is_safe_url(url):
        return url
    url = request.referrer
    if url and is_safe_url(url):
        return url
    return '/'
