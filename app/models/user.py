from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_database_connection, db
from datetime import datetime
import uuid


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    salt = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, email, password, first_name=None, last_name=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.salt = uuid.uuid4().hex
        self.password_hash = generate_password_hash(password + self.salt)
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password + self.salt)

    @staticmethod
    def get(user_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            user = User(id=user_data[0], username=user_data[1], password=user_data[2])
            return user
        else:
            return None
        
    def __repr__(self):
        return '<User {}>'.format(self.email)