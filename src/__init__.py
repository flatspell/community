from decouple import config
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemySessionUserDatastore

app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

# Registering blueprints
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

# Importing Models
from src.accounts.models import User, Role

login_manager.login_view = "accounts.login"

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401

@app.errorhandler(403)
def forbidden(error):
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500