import logging
import requests

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create a new user
url = 'http://127.0.0.1:5001/create_user'
data = {'name': 'John Doe', 'email': 'john.doe@example.com'}

# Send a POST request to the server
# The server will respond with a string
# that says "New user created successfully"
response = requests.post(url, data=data)

print(response.text)