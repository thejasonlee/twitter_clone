from flask import Flask, render_template, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userDatabase.db'
db = SQLAlchemy(app)

# Create user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    when_created = db.Column(db.DateTime, default = datetime.utcnow)


@app.route('/')
def home():
    """A starting place."""
    return render_template('home.html')

@app.route('/signin')
def signin():
    return 'Just a test'

@app.route('/signup')
def signup():
    return 'Just a fascinating second route. Really is something.'

@app.route('/route3/<int:my_value>')
def passing_a_simple_value_from_a_route(my_value):
    i_am_going_to_pass_this_variable = my_value
    return render_template('showing_a_value.html', context=i_am_going_to_pass_this_variable)


if __name__ == '__main__':
    app.run(debug=True)
