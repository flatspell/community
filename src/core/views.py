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
    return render_template('core.investment.html')

# @core_bp.route('/commerce')
# @login_required
# def commerce():
#     return render_template('commerce.html')

# @core_bp.route('/community')
# @login_required
# def community():
#     return render_template('community.html')

# @core_bp.route('/local_wealth_fund')
# @login_required
# def local_wealth_fund():
#     return render_template('local_wealth_fund.html')