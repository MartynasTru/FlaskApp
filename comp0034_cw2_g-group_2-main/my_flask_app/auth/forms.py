from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from my_flask_app.models import User


class SignupForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired()])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    email = EmailField(label='Email address', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for the given email address.')


class LoginForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label='Remember me')

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is None:
            raise ValidationError('This email address has not yet been registered to an account.')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            raise ValidationError('This email address has not yet been registered to an account.')
        if not user.check_password(password.data):
            raise ValidationError('Incorrect password.')


class ResetForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired()])

    # password = PasswordField(label='Password', validators=[DataRequired()])
    # password_repeat = PasswordField(label='Repeat Password',
    #                               validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is None:
            raise ValidationError('A password reset email has been sent to your email')


class AfterConfirmation(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            raise ValidationError('This email address has not yet been registered to an account.')
        if not user.check_password(password.data):
            raise ValidationError('Incorrect password.')
