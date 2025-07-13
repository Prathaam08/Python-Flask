from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired , Email  , Length

class RegistrationForm(FlaskForm):
    name = StringField("Full Name" , validators=[DataRequired(message="Name cannot be empty!!Please Type your Full Name")] )
    email = StringField("Email" , validators=[DataRequired() , Email() ])
    password = PasswordField("Password" , validators=[DataRequired(message="Password is required") , Length(min=6)])
    submit = SubmitField("Register")