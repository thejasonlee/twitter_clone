from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blahblahblah'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''Database configuration
If the environment variable 'DATABASE_URL' is defined, then use it.
Otherwise, default to the sqlite database.
'''
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL", f"sqlite:///userDatabase.db"
    )

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    db.create_all()
    manager.run()

