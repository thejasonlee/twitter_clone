"""
This file can be used to seed the sqlite3 database used in Gritter with fake data.
"""

import sqlite3


def fill(dbname):
    """ Function that seeds all tables in the sqlite3 database with filename 'dbname'.

        Parameters:
            dbname (str): the filename of the sqlite3 database used for Gritter.

        Returns:
             N/A
        """
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Start filling tables here

    return

