import os
import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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

    api_key = os.getenv('CENSUS_API_KEY')
    if not api_key:
        raise Exception("CENSUS_API_KEY environment variable not set")
    
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

if __name__ == '__main__':
    app.run(debug=True)