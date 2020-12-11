from flask import current_app
from project import db, login
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), nullable=True),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), nullable=True)
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship('Post', backref ='author', lazy='dynamic')
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id',
                                         backref='receiver', lazy='dynamic')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', 
                                         backref='author', lazy='dynamic')

    def already_follow(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() == 1   

    def follow(self, user):
        if self.already_follow(user) is False:
            self.followed.append(user)

    def unfollow(self, user):
        if self.already_follow(user) is True:
            self.followed.remove(user)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def generate_reset_password_token(self):
        return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm='HS256')

    def check_reset_password_token(self, token):
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            return User.query.filter_by(id=data['id']).first()
        except: 
            return

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    like_count = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('id: {self.id}, content:{self.content}, likes:{self.like_count}')"


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.content}')"


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text, nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Title: {}, Message: {}>'.format(self.title, self.body)
