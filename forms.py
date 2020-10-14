from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required!'), Length(min=5, max=20, message='Must be between 5 and 20 characters')])
    email = StringField('Email', validators=[InputRequired('An email is required!'), Length(min=5, max=50, message='Must be between 5 and 50 characters')])
    password = PasswordField('Password', validators=[InputRequired('A password is required!'), Length(min=5, max=20, message='Must be between 5 and 20 characters')])
    submit = SubmitField('Sign Up :D')

class UserPost(FlaskForm):
    content = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Post')
