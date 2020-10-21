'''
This file has been generated following the tutorial here:
https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/

The tutorial explains how to use Flask on Heroku with a database, and what configurations are required.

It also explains the commands that are needed when trying to run migrations. I.e. what to do
when you want to change the database schema.
'''

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from . import gritter

# Uses flask_script to create a new flask command 'db'. See https://flask-script.readthedocs.io/en/latest/
# Example usage: $ flask db --help
# This executes the db command (using flask-script) with the '--help' option
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


