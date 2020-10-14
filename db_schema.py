"""
This file defines the schema for the sqlite3 database used in Gritter.
"""

import sqlite3

def drop_tables(dbname):
    """ Function that drops all tables from the sqlite3 database with filename dbname.

        Parameters:
            dbname (str): the filename of the sqlite3 database used for Gritter.

        Returns:
             N/A
        """
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Start dropping tables here

    return

def create_tables(dbname):
    """ Function that creates the tables used for the gritter app. Builds tables in the file named dbname.

    Parameters:
        dbname (str): the filename of the sqlite3 database used for Gritter.

    Returns:
         N/A
    """
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Start building tables here
    return