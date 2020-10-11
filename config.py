from os import environ

# gets the 'PRODUCTION_ENVIRONMENT' variable from Heroku.
production = environ.get('PRODUCTION_ENVIRONMENT')

if production: # if the app is running in production (i.e. on Heroku)...
    DATABASE_URL = environ['DATABASE_URL']
    conn = psycoph2.connect(DATABASE_URL, sslmode='require')

else: # otherwise, use the Development database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userDatabase.db'



    conn = psycoph2.connect(DATABASE_URL, sslmode='require')



