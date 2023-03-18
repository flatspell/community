import os
import requests
from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/census_data')
def census_data():
    # Fetch data from the Census Bureau API using the requests library
    # and return the data as a JSON object
    pass
    e071b8af90ea338427066a202eeac7284dc62737

if __name__ == '__main__':
    app.run(debug=True)