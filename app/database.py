import logging
import os
import psycopg2

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()
logging.basicConfig(level=logging.DEBUG)

def get_database_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_DATABASE'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
    )

    return conn