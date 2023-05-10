from datetime import datetime

from flask_login import UserMixin

from src import bcrypt, db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, email, password, is_admin=False, is_confirmed=False, confirmed_at=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.created_at = datetime.now()
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed_at = confirmed_at

    def __repr__(self):
        return f"<email {self.email}>"