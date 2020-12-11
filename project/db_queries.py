"""
This file defines any queries needed to retrieve data from the sqlite3 database used in Gritter.
"""

import sqlite3
from project.models import Post, Like, User
from project import db, app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# -------------------------
# CONNECTION CONFIGURATION
# -------------------------
# Connect to the database
some_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# instantiate a Session object
session = Session()


# -------------------------
#     QUERY DEFINITIONS
# -------------------------
def get_likes_by_post_id(post_id):
    """returns count of likes for a given post id.
    Parameters:
        post_id (int): the id of the post of interest. I.e post.id.

    Returns:
        tuple (int, int): post.id, count of the number of likes for post.id.
    """

    likes = Like.query.filter_by(post_id=post_id).count()

    return (post_id, likes)


def get_username_by_id(user_id):
    username = User.query.filter(User.id == user_id).first()
    return username


def get_all_posts_with_like_counts():
    """returns a list of dictionaries, where each is a post that contains the post author and number of likes.
        Parameters:
            None.

        Returns:
            list (dict): each dict represents a post.
                keys: 'post', 'author', 'num_likes'
                values: post object and related data, post author, number of likes for the post
        """
    result = []
    posts = Post.query.order_by(Post.id.desc()).all()

    for post in posts:
        post_dict = {}
        post_dict['post'] = post

        user = get_username_by_id(post.user_id)
        if user is None:
            post_dict['author'] = 'user not found'
        else:
            post_dict['author'] = user.username


        num_likes = len(Like.query.filter(Like.post_id == post.id).all())
        post_dict['num_likes'] = num_likes

        result.append(post_dict)
    return result

def get_posts_with_string(expr):
    result = []
    posts = db.session.query(Post).filter(Post.content.contains(expr)).all()

    for post in posts:
        post_dict = {}
        post_dict['post'] = post

        user = get_username_by_id(post.user_id)
        if user is None:
            post_dict['author'] = 'user not found'
        else:
            post_dict['author'] = user.username


        num_likes = len(Like.query.filter(Like.post_id == post.id).all())
        post_dict['num_likes'] = num_likes

        result.append(post_dict)
    return result

def get_posts_by_user(userid):
    result = []
    posts = db.session.query(Post).filter(Post.user_id.contains(userid)).all()

    for post in posts:
        post_dict = {}
        post_dict['post'] = post

        user = get_username_by_id(post.user_id)
        if user is None:
            post_dict['author'] = 'user not found'
        else:
            post_dict['author'] = user.username

        num_likes = len(Like.query.filter(Like.post_id == post.id).all())
        post_dict['num_likes'] = num_likes

        result.append(post_dict)

    return result

def posts_of_following(following):
    result = []
    for users in following:
        result.append(get_posts_by_user(users))
    return result

