from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    webhookurl = StringField('Discord Webhook URL', validators=[DataRequired()])
    handles = StringField('Twitter Handles to Monitor', validators=[DataRequired()])
    submit = SubmitField('Submit')