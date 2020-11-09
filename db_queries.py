"""
This file defines any queries needed to retrieve data from the sqlite3 database used in Gritter.
"""

import sqlite3
from models import User, Post, Like
from gritter import db


def get_likes_by_post_id(post_id):
    """returns count of likes for a given post id.
    Parameters:
        post_id (int): the id of the post of interest. I.e post.id.

    Returns:
        tuple (int, int): post.id, count of the number of likes for post.id.
    """

    likes = Like.query.filter_by(post_id=post_id).count()

    return (post_id, likes)


def get_tweets():
    """ Returns all tweets from the sqlite3 database used in Gritter.

        Parameters:
            None.

        Returns:
             N/A

        Assumptions:
            - Database filename is 'gritter.db'
            - Tweets are in a table named 'tweet'
        """
    conn = sqlite3.connect('gritter.db')
    c = conn.cursor() # create a cursor object

    query = "SELECT * FROM tweet" # define the query

    c.execute(query) # execute the query

    return c.fetchall() # return all results of the query (see https://www.kite.com/python/examples/4265/sqlite3-get-all-rows-in-the-query-results)

# Define other functions here to perform other queries of the database