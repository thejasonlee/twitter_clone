from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

        # ***************************
        # **** MODEL DEFINITIONS ****
        # ***************************



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # password = db.Column(db.String(50), nullable=False)
    # email = db.Column(db.String(100), unique=True, nullable=False)
    # profile_photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    # when_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __repr__(self):
        return f"Post('{self.content}')"
