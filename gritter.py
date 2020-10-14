from flask import Flask, render_template, url_for, redirect, flash, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from forms import SignUpForm, UserPost
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blahblahblah'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profile_photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    when_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    content = db.Column(db.Text)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.timestamp}', '{self.content}')"


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


if __name__ == '__main__':
    app.run(debug=True)
