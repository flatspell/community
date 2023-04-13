from database import get_database_connection
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, request, url_for, redirect, flash
from models.user import User

auth = Blueprint('auth', __name__)
login_manager = LoginManager()

@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new user in the database
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        conn.commit()
        cursor.close()
        conn.close()

        return 'User registered successfully'

    return render_template('register.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # Process the login form data and authenticate the user
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.authenticate(username, password)

    if user:
        login_user(user)
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password')
        return redirect(url_for('login'))

@auth.route('/logout')
@login_required
def logout():
    # Log the user out and redirect to the home page
    logout_user()
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(user_id):
    # Load the User object for the specified user_id from your database
    return User.query.get(int(user_id))

@auth.route('/users/profile')
@login_required
def user_profile():
    # Fetch the user's profile information based on their user_id
    user_id = current_user.user_id
    print("User is authenticated: ", current_user.is_authenticated)
    # app.logger.debug("User is authenticated: %s", current_user.is_authenticated)
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id, ))
    user_data = cursor.fetchone()
    cursor.close()
    conn.close()

    if user_data:
        user = {'id': user_data[0], 'name': user_data[1], 'email': user_data[2]}
        return render_template('user_profile.html', user=user)
    else:
        return 'User not found'
    
@auth.route('/create_user', methods=['POST'])
def create_user():

    # app.logger.debug("Processing create user request")
    name = request.form['name']
    email = request.form['email']

    # app.logger.debug("Connecting to flatspell database")
    conn = get_database_connection()
    cursor = conn.cursor()

    # app.logger.debug("Inserting new user into users table")
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
    conn.commit()
    cursor.close()

    # app.logger.debug("Closing the connection to flatspell database")
    conn.close()

    return 'New user created successfully'