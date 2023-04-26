import logging
import os
import requests
from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
from database import get_database_connection

load_dotenv()

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.logger.setLevel(logging.DEBUG)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # load a user from the database based on the user_id
    return User.query.get(int(user_id))

@app.route('/account')
# @login_required
def account():
    # Fetch the user's profile information based on their user_id
    # user_id = current_user.user_id
    # user = User.get(user_id)
    
    return render_template('account.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/investment')
def investment():
    return render_template('investment.html')

@app.route('/small-business')
def small_business():
    return render_template('small-business.html')

@app.route('/commerce')
def commerce():
    return render_template('commerce.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/local_wealth_fund')
def local_wealth_fund():
    # return render_template('local_wealth_fund.html')
    return render_template('coming_soon.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
