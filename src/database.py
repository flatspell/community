import logging
import os
import requests
from flask import Flask, render_template, jsonify, request #, make_response, redirect
#from flask_basicauth import BasicAuth
from dotenv import load_dotenv
import psycopg2

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

def get_database_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_DATABASE'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
    )

    return conn