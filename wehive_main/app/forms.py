from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5)])
    email = EmailField('Email address', validators=[DataRequired()])
    new_password = PasswordField('Create a password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm the password', validators=[DataRequired(), EqualTo('new_password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign up')
