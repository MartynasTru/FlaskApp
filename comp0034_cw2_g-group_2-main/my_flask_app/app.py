from flask import render_template
from flask import send_file

import config
from __init__ import create_app
from __init__ import db
from my_flask_app.models import User

app = create_app(config.DevelopmentConfig)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html', title='Home page')


@app.route('/downloadpie')
def download_file_pie():
    return send_file('images/piechart.png', as_attachment=True)


@app.route('/downloadsingle')
def download_file_single():
    return send_file('images/singlebar.png', as_attachment=True)


@app.route('/downloadmulti')
def download_file_multi():
    return send_file('images/multibars.png', as_attachment=True)


@app.route('/downloadtable')
def download_file_table():
    return send_file('images/table.png', as_attachment=True)


@app.route('/downloadheat')
def download_file_heat():
    return send_file('images/heatmap.png', as_attachment=True)


@app.login_manager.user_loader
def load_user(user_id):
    """ Takes a user ID and returns a user object or None if the user does not exist"""
    if user_id is not None:
        return User.query.get(user_id)
    return None


if __name__ == '__main__':
    app.run(debug=True)
