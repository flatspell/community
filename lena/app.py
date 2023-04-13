import logging
from flask import Flask, render_template
from dotenv import load_dotenv
from database import db
from auth import auth, login_manager

load_dotenv()

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.register_blueprint(auth)
db.init_app(app)
login_manager.init_app(app)

app.logger.setLevel(logging.DEBUG)

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
    return render_template('local_wealth_fund.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
