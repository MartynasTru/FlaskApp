import pathlib
import os


# Flask config class
class Config(object):
    TESTING = False
    SECRET_KEY = 'hUzsj62spqThJnZpTyKT0Q'
    # Uses memory, not needed in this case
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('flask_app_db.sqlite'))
    UPLOADED_PHOTOS_DEST = pathlib.Path(__file__).parent.joinpath("static/img")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('businessnewscomp0034@gmail.com')
    MAIL_PASSWORD = os.getenv('123Mike123')


# Won't really be used for the cw
class ProductionConfig(Config):
    # A MySQL database on a server, used for the production environment
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

    # For activity, database set to sqlite file in data folder
    # SQLALCHEMY_DATABASE_URI = 'data/example.sqlite'
    pass


class DevelopmentConfig(Config):
    # Print database-related actions to console for debugging purposes
    SQLALCHEMY_ECHO = True
    # A local SQLite database, used for the development environment
    # DATA_PATH = pathlib.Path(__file__).parent.parent.joinpath("data")
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(DATA_PATH.joinpath('example.sqlite'))

    # For activity, database set to sqlite file in data folder
    # SQLALCHEMY_DATABASE_URI = 'data/example.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('flask_app_db.sqlite'))


class TestingConfig(Config):
    TESTING = True
    # Print database-related actions to console for debugging purposes
    SQLALCHEMY_ECHO = True
    # An in memory SQLite database, not saved to disk, used for the testing environment
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # For activity, database set to sqlite file in data folder
    # SQLALCHEMY_DATABASE_URI = 'data/example.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('flask_app_db.sqlite'))
