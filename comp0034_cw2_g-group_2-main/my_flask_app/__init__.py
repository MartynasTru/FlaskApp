from flask import Flask
from flask_login import LoginManager, login_required
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import get_root_path
import dash_bootstrap_components as dbc
from dash import Dash
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_mail import Mail
from flask_jwt_extended import JWTManager

csrf = CSRFProtect()
csrf._exempt_views.add('dash.dash.dispatch')

db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)

login_manager = LoginManager()

mail = Mail()

jwt = JWTManager()


def create_app(config_class_name):
    """
    Initialise the Flask application.
    :type config_class_name: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """

    app = Flask(__name__)

    app.config.from_object(config_class_name)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'businessnewscomp0034@gmail.com'
    app.config['MAIL_PASSWORD'] = '123Mike123'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    csrf.init_app(app)

    db.init_app(app)

    configure_uploads(app, photos)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'Please log in to access this page.'
    register_dashapp(app)
    jwt.init_app(app)

    mail.init_app(app)

    with app.app_context():
        from my_flask_app.models import User
        db.create_all()

    from my_flask_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from my_flask_app.main.routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app


def register_dashapp(app):
    from my_dash_app import layout
    from my_dash_app.callbacks import register_callbacks

    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=3, shrink-to-fit=yes"}

    dashapp = Dash(__name__,
                   server=app,

                   assets_folder=get_root_path(__name__) + '/dashboard/assets/',
                   meta_tags=[meta_viewport],
                   external_stylesheets=[dbc.themes.SKETCHY],
                   routes_pathname_prefix='/dash/')

    with app.app_context():
        dashapp.title = 'Dashboard'
        dashapp.layout = layout.layout
        register_callbacks(dashapp)

    _protect_dash_views(dashapp)


def _protect_dash_views(dash_app):
    for view_func in dash_app.server.view_functions:
        if view_func.startswith(dash_app.config.routes_pathname_prefix):
            dash_app.server.view_functions[view_func] = login_required(dash_app.server.view_functions[view_func])
