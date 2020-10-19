from app import db
from datetime import datetime
'''
        ***************************
        **** MODEL DEFINITIONS ****
        ***************************
'''

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

