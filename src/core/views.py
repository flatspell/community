from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)

@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")

@core_bp.route('/investment')
@login_required
def investment():
    return render_template('core/investment.html')

@core_bp.route('/account')
@login_required
def account():
    return render_template('core/account.html')

@core_bp.route('/commerce')
@login_required
def commerce():
    return render_template('commerce.html')

@core_bp.route('/community')
@login_required
def community():
    return render_template('community.html')