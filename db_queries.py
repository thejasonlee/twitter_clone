"""
This file defines any queries needed to retrieve data from the sqlite3 database used in Gritter.
"""

import sqlite3

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