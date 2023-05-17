from flask import Blueprint, render_template
from flask_login import login_required

from src.utils.decorators import check_is_confirmed, roles_required

core_bp = Blueprint("core", __name__)

@core_bp.route("/")
@login_required
@check_is_confirmed
@roles_required('admin', 'investor', 'economic_developer')
def home():
    return render_template("core/index.html")

@core_bp.route('/investment')
@login_required
@check_is_confirmed
@roles_required('admin', 'investor', 'economic_developer')
def investment():
    return render_template('core/investment.html')

@core_bp.route('/account')
@login_required
@check_is_confirmed
@roles_required('admin')
def account():
    return render_template('core/account.html')

@core_bp.route('/commerce')
@login_required
@check_is_confirmed
@roles_required('admin', 'economic_developer')
def commerce():
    return render_template('core/commerce.html')

@core_bp.route('/community')
@login_required
@check_is_confirmed
@roles_required('admin', 'investor', 'entrepreneur', 'economic_developer')
def community():
    return render_template('core/community.html')