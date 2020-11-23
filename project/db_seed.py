"""
This file can be used to seed the sqlite3 database used in Gritter with fake data.
"""

import sqlite3
from project.models import User, Post, Like
from random import seed, randint
from project import db
from faker import Faker

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

def fill_posts():
    """Generates post data in database"""
    #use faker to generate 100 random strings
    makePosts = Faker()
    new_posts = []
    for i in range(100):
        new_posts.append(makePosts.text())

    for j in new_posts:
        post = Post(j, 0)
        db.session.add_all(post)  # add the likes to the session
        db.session.commit()  # commit the session to the database


    return



def fill_all_tables():
    """ Master function, that calls all other db_seed functions, to fill in dummy data in the database."""

    fill_tweet()

    # list all other fix_XXX() functions here
    # example 1: fill_users()
    # example 2: fill_posts()
    # example 3: fill_likes()

    return