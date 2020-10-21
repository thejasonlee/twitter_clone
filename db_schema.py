# SQL Commands for establishing db schema

def tweet():
    # create a table here
    conn = db.conenction()
    query = "CREATE TABLE TWEET(" \
            "tweet_id INT AUTO_INCREMENT," \
            "body VARCHAR(144)," \
            "PRIMARY KEY (tweet_id));"
    conn.execute(query)
    return


def createUserTable():
    conn = db.conenction()
    query = "CREATE table User"
    conn.execute(query)
    return


def buildTables():
    tweet()