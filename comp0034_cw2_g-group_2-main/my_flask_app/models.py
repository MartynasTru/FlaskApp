import os
from datetime import datetime

# MAIL
import jwt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from __init__ import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_token(self, user_id):
        try:
            payload = {
                'reset_password': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            print('encode: ', jwt.encode(
                payload,
                key=os.getenv('SECRET_KEY'),
                algorithm='HS256'
            ))
            return jwt.encode(
                payload,
                key=os.getenv('SECRET_KEY'),
                algorithm='HS256'
            )

        except Exception as e:
            return e

    @staticmethod
    def verify_email(email):

        user = User.query.filter_by(email=email).first()

        return user

    @staticmethod
    def verify_reset_token(token):
        try:
            payload = jwt.decode(token, key=os.getenv('SECRET_KEY'), algorithm='HS256')
            print('payload: ', payload)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email} {self.password}"
