from flask import Flask, render_template, url_for, redirect, flash, send_from_directory, request
from forms import SignUpForm, UserPost
from models import User, Post
from app import app
import db_schema as db_schema
import db_seed as db_seed

from flask_migrate import Migrate, MigrateCommand
from app import db


@app.route('/db_build')
def start_our_database_over():
    # drop all tables

    # re-build all tables by calling appropriate function in db_schema.py
    db_schema.buildTables()

    # fill in all dummy data by calling function in db_seed.py
    db_seed.fillAllTables()

    # redirect to https://gritter-3308.herokuapp.com/
    redirect(url_for('home'))
    return

'''
MVC -- 
Model: Define tables in the database (db_schema.py)
View: UI that a user sees (templates)
Controller: 'business logic' -- what methods/functions are run when a route is visited.
'''


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
