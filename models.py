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
    like = db.Column(db.Integer)

    def __repr__(self):
        return f"Post('{self.content}')"


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Text)
    # user_id = db.Column(db.Integer, foreign_key
    count = db.Column(db.Integer)

    def __repr__(self):
        return f"Post('{self.content}')"