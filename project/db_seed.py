"""
This file can be used to seed the sqlite3 database used in Gritter with fake data.
"""

import sqlite3
from project.models import User, Post, Like
from random import seed, randint
from project import db, bcrypt
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
def create_admin_user():
    hashed_pw = bcrypt.generate_password_hash("admin").decode('utf-8')
    user = User(username="admin", email="admin@gritter.com", password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return


def empty_user():
    users = User.query.all()
    for user in users:
        # delete their Likes
        Like.query.filter(Like.user_id == user.id).delete()

        # delete their Posts
        Post.query.filter(Post.user_id == user.id).delete()

        # delete the user
        User.query.filter(User.id == user.id).delete()
    create_admin_user()
    return


def fill_user():
    empty_user()

    # use Faker to generate users.
    num_users_to_generate = 100
    fake = Faker()
    for i in range(num_users_to_generate):
        temp_username = fake.unique.last_name() + str(i)
        temp_password = 'admin'
        temp_hashed_pw = bcrypt.generate_password_hash(temp_password).decode('utf-8')
        temp_email = fake.unique.email()
        temp_user = User(username=temp_username, password=temp_hashed_pw, email=temp_email)
        db.session.add(temp_user)
        #db.session.execute('INSERT INTO "user" (username, password, email) VALUES (:param1, :param2, :param3);', {'param1': makeUsers.unique.last_name() + str(i), 'param2': '$2b$12$8oFObtgF/omzn/5jD0YSpe.ZphcX2G3lqqym9drbwZjJE7o6ubMmi', 'param3': makeUsers.unique.email()})
        db.session.commit()
    fake.unique.clear() # see https://faker.readthedocs.io/en/master/index.html?highlight=unique#unique-values

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

        # 10% of all users will like each post
        # for each user
        for user in users:
            # 10% of the time..
            if randint(0, 10) > 8:
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

    # Configuring for random data generation
    seed(1) # for posts
    fake = Faker() # for timestamp. See https://faker.readthedocs.io/en/master/index.html
    Faker.seed(0) # See https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html

    # Cycle through all users.
    # Generate 0-9 posts per user.
    # Use Faker library to randomise username generation and post timestamps.
    users = User.query.all()
    for user in users:
        # 0-9 posts
        for i in range(0, randint(0,10)):
            # data for a temporary post
            temp_content = fake.text()
            temp_timestamp = fake.date_time()
            temp_userid = user.id

            # create and add temporary Post object to database
            temp_post = Post(content = temp_content, timestamp=temp_timestamp, user_id=temp_userid)
            db.session.add(temp_post)
            # db.session.execute('INSERT INTO post (content) VALUES (:param);', {'param':makePosts.text()})
            db.session.commit()  # commit the session to the database
    return
