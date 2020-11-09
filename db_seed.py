"""
This file can be used to seed the sqlite3 database used in Gritter with fake data.
"""

import sqlite3
from models import User, Post, Like
from random import seed, randint
from gritter import db


def fill_user():
    conn = sqlite3.connect("gritter")
    c = conn.cursor()

    # Start filling tables here
    users = ['admin']
    query = "INSERT INTO USER(tweet_id, body) VALUES(19, " + placeholder_body + ");"
    c.execute(query)
    return


def fill_tweet():
    """ Function that seeds all tables in the sqlite3 database with filename 'dbname'.

        Parameters:

        Returns:
             N/A
        """
    conn = sqlite3.connect("gritter")
    c = conn.cursor()

    # Start filling tables here
    placeholder_body = "sample tweets are awesome!"
    query = "INSERT INTO TWEET(tweet_id, body) VALUES(19, " + placeholder_body + ");"
    c.execute(query)

    # fills in table function1

    return

def fill_likes():
    """Generates fake 'like' data in the database."""

    posts = Post.query.all() # get all posts
    users = User.query.all() # get all users

    likes = []
    seed(1)  # seed the random number generator
    for post in posts:
        # for each user
        for user in users:
            # 50% of the time..
            if randint(0, 10) > 4:
                # generate a like
                likes.append(Like(post_id=post.id, user_id=user.id))

    db.session.add_all(likes) # add the likes to the session
    db.session.commit()       # commit the session to the database

    # update post.like_count values

    return

def empty_likes():
    """Empties existing 'like' table of any data."""

    return

def fill_all_tables():
    """ Master function, that calls all other db_seed functions, to fill in dummy data in the database."""

    fill_tweet()

    # list all other fix_XXX() functions here
    # example 1: fill_users()
    # example 2: fill_posts()
    # example 3: fill_likes()

    return