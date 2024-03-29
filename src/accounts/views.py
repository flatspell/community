from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from flask_security import SQLAlchemySessionUserDatastore

from src import bcrypt, db
from src.accounts.models import User, Role, Network
from src.accounts.token import confirm_token, generate_token
from src.utils.decorators import logout_required
from src.utils.email import send_email

from .forms import RegisterForm, LoginForm

accounts_bp = Blueprint("accounts", __name__)

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)

@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        role_name = form.role.data
        network_name = form.community.data

        role = Role.query.filter_by(name=role_name).first()
        network = Network.query.filter_by(name=network_name).first()

        if role:
            user = User(email=form.email.data, password=form.password.data, network_id=network)
            user.roles.append(role)

            db.session.add(user)
            db.session.commit()

        token = generate_token(user.email)
        confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
        html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)
        flash("A confirmation email has been sent via email.", "success")

        if user.has_roles("entrepreneur"):
            return redirect(url_for("core.community"))
        else:
            return redirect(url_for("core.home"))

    return render_template("accounts/register.html", form=form)

@accounts_bp.route("/login", methods=["GET", "POST"])
@logout_required
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        if user.has_roles("entrepreneur"):
            return redirect(url_for("core.community"))
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        # user = User.query.filter_by(email=form.email.data).first()
        user = user_datastore.find_user(email=form.email.data)
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            if user.has_roles("entrepreneur"):
                return redirect(url_for("core.community"))
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("accounts/login.html", form=form)
    return render_template("accounts/login.html", form=form)

@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login"))

@accounts_bp.route("/confirm/<token>")
@login_required
def confirm_email(token):
    if current_user.is_confirmed:
        flash("Account already confirmed.", "success")
        return redirect(url_for("core.home"))
    email = confirm_token(token)
    user = User.query.filter_by(email=current_user.email).first_or_404()
    if user.email == email:
        user.is_confirmed = True
        user.confirmed_at = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash("You have confirmed your account. Thanks!", "success")
    else:
        flash("The confirmation link is invalid or has expired.", "danger")
    return redirect(url_for("core.home"))

@accounts_bp.route("/inactive")
@login_required
def inactive():
    if current_user.is_confirmed:
        return redirect(url_for("core.home"))
    return render_template("accounts/inactive.html")

@accounts_bp.route("/resend")
@login_required
def resend_confirmation():
    if current_user.is_confirmed:
        flash("Your account has already been confirmed.", "success")
        return redirect(url_for("core.home"))
    token = generate_token(current_user.email)
    confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
    html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash("A new confirmation email has been sent.", "success")
    return redirect(url_for("accounts.inactive"))