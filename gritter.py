from flask import Flask, render_template, url_for, redirect, flash, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
#from forms import SignUpForm, UserPost
#from models import User, Post


# create a Flask object
app = Flask(__name__)

'''
    ******************************
    Flask app object configuration
    ******************************
'''
# Establish a secret key
app.config['SECRET_KEY'] = 'blahblahblah'

# Suppress the SQLALCHEMY_TRACK_MODIFICATIONS warnings in server loggin
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database configuration
# If the environment variable 'DATABASE_URL' is defined, then use it.
# Otherwise, default to the sqlite database.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL", f"sqlite:///userDatabase.db"
    )



'''
    **********************************
            SQLAlchemy Setup 
    **********************************
'''
# create SQLAlchemy object
db = SQLAlchemy(app)

# create Migrate object. See https://flask-migrate.readthedocs.io/en/latest/
migrate = Migrate(app, db)

'''
    **********************************
                ROUTES
    **********************************
'''

# @app.route('/')
# def hello_world():
#     return render_template('test.html')

@app.route('/')
def home():
    form = UserPost()

    if form.is_submitted():
        post = Post(content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user_home'))
    posts = Post.query.all()
    return render_template('user_home.html', form=form, posts=posts)

@app.route('/signin')
def signin():
    return render_template('signIn.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        getback = request.form
        # line here to save the form data into the database
        return render_template('user.html', getback = getback)

    if form.validate_on_submit():
        return render_template('user.html')
    return render_template('signUp.html', form = form)


# @app.route('/user/home')
# def user_home():
#     posts = Post.query.all()
#     return render_template('user_home.html', posts=posts)   


@app.route('/user/home', methods=['GET', 'POST'])
def user_home():
    form = UserPost()
    if form.is_submitted():
        post = Post(content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user_home'))
    posts = Post.query.all()
    return render_template('user_home.html', form=form, posts=posts)


@app.route('/db_build')
def start_our_database_over():
    """ An example function to show how a route can be used to rebuild and reseed the database.

    This route can be associated with a button in the navbar to make it easy to rebuild.
    Note: The button, and its associated route, has not been implemented in a template file.
    """

    # drop all tables (has not been implemented yet)

    # re-build all tables by calling appropriate function in db_schema.py
    db_schema.buildTables()

    # fill in all dummy data by calling function in db_seed.py
    db_seed.fill_all_tables()

    # redirect to https://gritter-3308.herokuapp.com/
    redirect(url_for('home'))
    return



if __name__ == '__main__':
    app.run(debug=True)