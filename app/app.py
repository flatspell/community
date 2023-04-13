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

# login_manager = LoginManager()
# login_manager.init_app(app)


# @app.route('/login')
# def login():
#     # Render the login page
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login_post():
#     # Process the login form data and authenticate the user
#     username = request.form.get('username')
#     password = request.form.get('password')

#     user = User.authenticate(username, password)

#     if user:
#         login_user(user)
#         return redirect(url_for('home'))
#     else:
#         flash('Invalid username or password')
#         return redirect(url_for('login'))

# @app.route('/logout')
# @login_required
# def logout():
#     # Log the user out and redirect to the home page
#     logout_user()
#     return redirect(url_for('home'))

@app.route('/users/profile')
@login_required
def user_profile():
    # Fetch the user's profile information based on their user_id
    user_id = current_user.user_id
    user = User.get(user_id)
    
    return render_template('user_profile.html', user=user)

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

# @app.route('/users/<int:user_id>')
# def user_profile(user_id):
#     conn = get_database_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     user_data = cursor.fetchone()
#     cursor.close()
#     conn.close()

#     if user_data:
#         user = {'id': user_data[0], 'name': user_data[1], 'email': user_data[2]}
#         return render_template('user_profile.html', user=user)
#     else:
#         return 'User not found'

# @app.route('/create_user', methods=['POST'])
# def create_user():

#     app.logger.debug("Processing create user request")
#     name = request.form['name']
#     email = request.form['email']

#     app.logger.debug("Connecting to flatspell database")
#     conn = get_database_connection()
#     cursor = conn.cursor()

#     app.logger.debug("Inserting new user into users table")
#     cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
#     conn.commit()
#     cursor.close()

#     app.logger.debug("Closing the connection to flatspell database")
#     conn.close()

#     return 'New user created successfully'



# @app.route('/heatmap.js')
# def heatmap_js():
#     js_dir = os.path.join(app.root_path, 'static', 'js')
#     return send_from_directory(js_dir, 'heatmap.js')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
