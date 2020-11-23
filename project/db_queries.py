"""
This file defines any queries needed to retrieve data from the sqlite3 database used in Gritter.
"""

import sqlite3
from project.models import User, Post, Like
from project import db


def get_likes_by_post_id(post_id):
    """returns count of likes for a given post id.
    Parameters:
        post_id (int): the id of the post of interest. I.e post.id.

    Returns:
        tuple (int, int): post.id, count of the number of likes for post.id.
    """

    likes = Like.query.filter_by(post_id=post_id).count()

    return (post_id, likes)
