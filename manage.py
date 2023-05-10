from datetime import datetime
from flask.cli import FlaskGroup
from src import app, db
from src.accounts.models import User
import getpass

cli = FlaskGroup(app)

@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    email = input("Enter email address: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return 1
    else:
        try:
            user = User(
                    email=email,
                    password=password,
                    is_admin=True,
                    is_confirmed=True,
                    confirmed_at=datetime.now()
            )
            db.session.add(user)
            db.session.commit()
            print(f"Admin with email {email} created succesfully.")
        except Exception:
            print("Failed to create admin user.")

if __name__ == "__main__":
    cli()