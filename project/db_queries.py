"""
This file defines any queries needed to retrieve data from the sqlite3 database used in Gritter.
"""

import sqlite3
from project.models import Post, Like
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


def get_all_posts_with_like_counts():
    result = []
    posts = Post.query.all()

    for post in posts:
        likes = Like.query.filter(Like.post_id == post.id).all()
        result.append((post, likes))

    return result
