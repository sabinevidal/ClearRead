from flask_wtf import FlaskForm
from wtforms import Form, Field, BooleanField, StringField, IntegerField, validators, TextField, SubmitField
from wtforms.fields.core import FormField
from wtforms.fields.simple import HiddenField
from wtforms.widgets import TextInput
from .models import *
from wtforms.validators import DataRequired, Email, Length

class ExmpleForm(FlaskForm):
    name = StringField('LABEL', [DataRequired()])
    email = StringField(
            'Email',
            [
                Email(message=('Not a valid email address.')),
                DataRequired()
            ]
    )