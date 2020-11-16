from flask import flash, render_template, url_for, redirect, g, send_from_directory, request
from project import app, db, login
from project.forms import SignUpForm, SignInForm, UserPost
from project.models import User, Post, Like
from project.db_seed import *
from project.db_queries import *
from flask_login import current_user, login_user, logout_user, login_required
from project import bcrypt



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username=form.username.data
        email =form.email.data
        hashed_pw = bcrypt.generate_password_hash(form.password.data.encode('utf-8'))
        user = User(username=username, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('user_home'))
    return render_template('signUp.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        pw_check = bcrypt.check_password_hash(user.password, form.password.data.encode('utf-8'))
        if user is None or not pw_check:
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('signIn.html', form=form)


    # #creating a dictionary to store various kinds of data to be passed to the template.
    # # If the data is passed to the template, then I can 'print' it to the page.
    # context = {}

    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()

    #     # I want a list of all users. If there are any, save to context.
    #     users = User.query.all()
    #     if users:
    #         context['users'] = users

    #     if user:
    #         # I'm curious what 'user' is, so I'll save it to context.
    #         context['user_value'] = user

    #         if(user.password == form.password.data):
    #             # save some of the data in context
    #             context['user_pwd'] = user.password
    #             context['form_pwd_data'] = form.password.data

    #             #login_user(user, remember=form.remember.data)

    #             # return with context dictionary, which holds data for template 'printing'
    #             return render_template('home.html', context=context) + 'Hello, ' + form.username.data

    #     # this path only occurs if the login fails
    #     return render_template('signIn.html', form=form)
    # return render_template('signIn.html', form=form)


@app.route('/signout')
@login_required
def signout():
    # Sign out using flask-login built in function
    logout_user()
    return redirect(url_for('signin'))


@app.route('/user/home', methods=['GET', 'POST'])
@login_required
def user_home():

    form = UserPost()
    if form.validate_on_submit():
        post = Post(content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user_home'))

    # get all posts
    posts = Post.query.all()

    # calculate the number of likes for each post
    like_counts = []
    for post in posts:
        like_counts.append(get_likes_by_post_id(post.id))

    return render_template('user_home.html', form=form, posts=posts, likes=like_counts)


@app.route('/likes', methods=['POST', 'GET'])
def show_likes():

    # get likes and posts for context
    likes = Like.query.all()
    posts = Post.query.all()

    return render_template('likes.html', likes=likes, posts=posts)


@app.route('/likes/fill', methods=['GET'])
def create_likes():
    # drop all likes (this is imported from db_seed)
    empty_likes()

    # create likes (this is imported from db_seed)
    fill_likes()

    flash(message='Created likes.')
    return redirect(url_for('show_likes'))


@app.route('/likes/delete', methods=['GET'])
def delete_likes():
    # drop all likes (this is imported from db_seed)
    empty_likes()

    flash('Deleted likes.', 'error')
    return redirect(url_for('show_likes'))


@app.route('/click_like', methods=['GET'])
def click_like(pst_id, usr_id):

    like = Like.query.filter(post_id=pst_id, user_id=usr_id)
    if like.count() == 0:
        # create and save like object
        temp_like = Like(user_id=usr_id, post_id=pst_id)
        db.session.add(temp_like)
    else:
        # delete like object
        like.delete()
    db.session.commit()

    return redirect(url_for('user_home'))