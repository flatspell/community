from functools import wraps

from flask import flash, redirect, url_for, abort
from flask_login import current_user


def logout_required(func):
  @wraps(func)
  def decorated_function(*args, **kwargs):
      if current_user.is_authenticated:
          flash("You are already authenticated.", "info")
          return redirect(url_for("core.home"))
      return func(*args, **kwargs)

  return decorated_function

def check_is_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed is False:
            flash("Please confirm your account!", "warning")
            return redirect(url_for("accounts.inactive"))
        return func(*args, **kwargs)

    return decorated_function

def roles_required(*roles):
    def decorated_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated or not current_user.has_roles(*roles):
                abort(403)  # Or redirect to a 403 Forbidden page
            return func(*args, **kwargs)
        return wrapper
    return decorated_function