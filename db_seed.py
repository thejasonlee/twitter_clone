"""
This file can be used to seed the sqlite3 database used in Gritter with fake data.
"""

from db_schema import tweet

import sqlite3


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


def fill_all_tables():
    """ Master function, that calls all other db_seed functions, to fill in dummy data in the database."""

    fill_tweet()

    return