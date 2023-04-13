import logging
import os
from dotenv import load_dotenv
import psycopg2
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

db = SQLAlchemy()

# Set the database URI
database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
if not database_uri:
    raise RuntimeError('SQLALCHEMY_DATABASE_URI is not set in environment variables.')

# Configure the database
db.app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(db.app)

def get_database_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_DATABASE'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
    )

    return conn

