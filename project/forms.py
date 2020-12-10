from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length, EqualTo, Email


class SignUpForm(FlaskForm):
    username= StringField('Username',validators=[InputRequired(), Length(min=5, max=30, message='Must be between 5 and 30 characters')])
    email= StringField('Email',validators=[InputRequired(), Email()])
    password= PasswordField('Password', validators=[InputRequired(), Length(min=5, max=30, message='Must be between 5 and 30 characters')])
    confirmPassword = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password'), Length(min=5, max=30, message='Must be between 5 and 30 characters')])
    submit= SubmitField("Sign Up :D")


class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In :P')


class UserPost(FlaskForm):
    content = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Post')


class FollowForm(FlaskForm):
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    content = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


