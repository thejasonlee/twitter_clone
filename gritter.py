from flask import Flask, render_template, url_for, redirect, flash, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from forms import SignUpForm, UserPost
from manage import User, Post

from flask_migrate import Migrate, MigrateCommand


@app.route('/')
def home():
    form = UserPost() # <-- UserPost() object being instantiated here.

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


if __name__ == '__main__':
    app.run(debug=True)
