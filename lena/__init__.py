from flask import Flask
from auth import auth

app = Flask(__name__)
auth.init_app(app)