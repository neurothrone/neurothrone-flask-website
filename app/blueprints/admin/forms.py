from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

from app.blueprints.admin.model import Admin


class LoginForm(FlaskForm):
    pass
