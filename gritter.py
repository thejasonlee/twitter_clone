from flask import Flask, render_template, url_for, redirect, flash, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from structures import SignUpForm 
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'blahblahblah'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userDatabase.db'
db = SQLAlchemy(app)

# Create user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    profile_photo = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    when_joined = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



@app.route('/')
def home():
    """A starting place."""
    return render_template('home.html')

@app.route('/signin')
def signin():
    return 'Just a test'

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        getback = request.form
        return render_template('user.html', getback = getback)
    return render_template('signUp.html', form = form)   


@app.route('/route3/<int:my_value>')
def passing_a_simple_value_from_a_route(my_value):
    i_am_going_to_pass_this_variable = my_value
    return render_template('showing_a_value.html', context=i_am_going_to_pass_this_variable)


if __name__ == '__main__':
    app.run(debug=True)
