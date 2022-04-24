from flask import render_template
from flask_mail import Message

from my_flask_app import mail


def send_email(user):
    token = user.get_reset_token(user.id)

    msg = Message('Hello', sender='businessnewscomp0034@gmail.com', recipients=[user.email])
    msg.subject = "Flask App Password Reset"
    msg.html = render_template('resetconfirmation.html', user=user, token=token)

    mail.send(msg)
