# pip3 install Flask-SQLAlchemy psycopg2
# pip install psycopg2
# init make sure to initialize our taskmanager application as a package, allowing us to use
#our own imports, as well as any standard imports.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"): 
    import env  # noqa


app = Flask(__name__) 
# we create an instance of the imported Flask() class, and that will be stored in
# a variable called 'app', which takes the default Flask __name__ module.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes  # noqa