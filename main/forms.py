from flask_wtf import FlaskForm
from wtforms import Form, Field, BooleanField, StringField, IntegerField, validators, SubmitField, EmailField
from wtforms.fields.simple import HiddenField
from wtforms.widgets import TextInput
from .models import *
from wtforms.validators import DataRequired, Email, Length

class ExmpleForm(FlaskForm):
    name = StringField('LABEL', [DataRequired()])
    email = EmailField(
            'Email',
            [
                Email(message=('Not a valid email address.')),
                DataRequired()
            ]
    )