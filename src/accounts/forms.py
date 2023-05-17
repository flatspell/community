from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User


class RegisterForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", 
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    role = SelectField(
        "What is your role?",
        choices=[
            ("investor", "Investor"),
            ("entrepreneur", "Entrepreneur"),
            ("economic_developer", "Economic Development Council"),
            ("economic_developer", "Chamber of Commerce"),
            ("economic_developer", "Nonprofit"),
            ("entrepreneur", "Other"), 
            # Set other to entrepreneur for now because it has least privileges
            # We can override other to whatever role is most appropriate later
        ],
        validators=[DataRequired()]
    )
    community = SelectField(
        "Which community are you in?",
        choices=[
            ("clallam_wa", "Clallam County, WA"),
            ("jefferson_wa", "Jefferson County, WA"),
        ],
        validators=[DataRequired()]
    )

    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate(extra_validators)
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True
    
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])