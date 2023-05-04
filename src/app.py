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
    return render_template('account.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/census_data')
def census_data():
    try:
        data = get_census_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_census_data():
    api_key = os.getenv('US_CENSUS_API_KEY')
    if not api_key:
        raise Exception("US_CENSUS_API_KEY environment variable not set")
    
    url = f"https://api.census.gov/data/2019/acs/acs5?get=NAME,B01003_001E,B19013_001E&for=place:54365&in=state:53&key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        headers = data[0]
        values = data[1]

        result = {}
        for i, header in enumerate(headers):
            result[header] = values[i]

        return result
    else:
        raise Exception(f"Failed to fetch data from US Census Bureau API. Status code: {response.status_code}")

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
    return render_template('local_wealth_fund.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
