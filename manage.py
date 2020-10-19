from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import date
import os


app = Flask(__name__)

'''Database configuration
If the environment variable 'DATABASE_URL' is defined, then use it.
Otherwise, default to the sqlite database.
'''
_default_sqlite_db = "userDatabase.db"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL", f"sqlite:///{_default_sqlite_db}"
    )

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

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


if __name__ == '__main__':
    manager.run()

