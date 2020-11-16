from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

        # ***************************
        # **** MODEL DEFINITIONS ****
        # ***************************



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    like_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Post('id: {self.id}, content:{self.content}, likes:{self.like_count}')"


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f"Post('{self.content}')"


class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    follow_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

     def __repr__(self):
        return f"Follow('{self.follower_id}', '{self.follow_id}')"
