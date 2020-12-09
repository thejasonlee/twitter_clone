"""
This file can be used to seed the sqlite3 database used in Gritter with fake data.
"""

import sqlite3
from project.models import User, Post, Like
from random import seed, randint
from project import db
from faker import Faker


# --------------------------
# Master functions that call other functions.
# The subordinate functions control data at the table level.
# Master functions will seed (and/or empty) all tables.
# --------------------------

def empty_all_tables():
    """Empties data from all tables."""

    empty_likes()
    empty_posts()
    empty_user()
    return

def fill_all_tables():
    """Calls all other db_seed functions to fill in dummy data in the database."""

    # remove all legacy data
    empty_all_tables()

    # seed all tables with new data
    fill_user()
    fill_posts()
    fill_likes()

    return


# --------------------------
# SEED and EMPTY USER table
# --------------------------
def empty_user():
    db.session.execute("""DELETE FROM "user" WHERE username != ('admin');""")
    db.session.commit()

    # if no admin/admin account exists, create it.
    admin_user_present = User.query.filter(User.username == 'admin').first()
    if admin_user_present is None:
        db.session.execute('INSERT INTO "user" (username, password, email) VALUES ("admin", "admin", "admin@gritter.com");')
        db.session.commit()  # commit the session to the database
    return

def fill_user():
    empty_user()

    # use Faker library to generate fake users.
    makeUsers = Faker()
    for i in range(100):
        db.session.execute('INSERT INTO "user" (username, password, email) VALUES (:param1, :param2, :param3);', {'param1': makeUsers.unique.last_name() + str(i), 'param2': '$2b$12$8oFObtgF/omzn/5jD0YSpe.ZphcX2G3lqqym9drbwZjJE7o6ubMmi', 'param3': makeUsers.unique.email()})
        db.session.commit()  # commit the session to the database
    makeUsers.unique.clear()

    return


# --------------------------
# SEED and EMPTY LIKE table
# --------------------------
def fill_likes():
    """Generates fake 'like' data in the database."""

    posts = Post.query.all() # get all posts
    users = User.query.all() # get all users

    seed(1)  # seed the random number generator

    for post in posts:
        # for each post, we are going to generate several likes.
        # We create the like objects and update the post.like_count attribute.
        # then we commit all the changes to the database and iterate to the next post.
        likes = []          # holds all 'like' objects for a given post
        like_count = 0      # accumulator for post.like_count

        # 50% of all users will like each post
        # for each user
        for user in users:
            # 50% of the time..
            if randint(0, 10) > 4:
                # generate a like object and save to 'likes', and +like_count
                likes.append(Like(post_id=post.id, user_id=user.id))
                like_count += 1

        post.like_count = like_count # update post.like_count
        db.session.add_all(likes) # add the likes to the session
        db.session.commit()       # commit the session to the database

    return

def empty_likes():
    """Empties existing 'like' table of any data."""
    Like.query.delete()
    db.session.commit()

    # set all post.like_count to 0
    posts = Post.query.all()
    for post in posts:
        if post.like_count != 0:
            post.like_count = 0
    db.session.commit()
    return



# --------------------------
# SEED and EMPTY POST table
# --------------------------

def empty_posts():
    empty_likes()
    db.session.execute('DELETE FROM post;')
    db.session.commit()

    return

def fill_posts():
    """Empties all Post data, then generates fake posts using Faker."""

    # empty legacy data
    empty_posts()

    #use faker to generate 100 random strings and insert into db
    makePosts = Faker()
    for i in range(100):
        db.session.execute('INSERT INTO post (content) VALUES (:param);', {'param':makePosts.text()})
        db.session.commit()  # commit the session to the database
    return
