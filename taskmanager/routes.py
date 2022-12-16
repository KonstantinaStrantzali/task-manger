from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

""" 
create this 'taskmanager' database, navigate to the Terminal, and login to the Postgres CLI by typing 'psql' and hitting enter.
To create the database, we can simply type: CREATE DATABASE taskmanager;
Once that's created, we'll switch over to that connection by typing:
\c taskmanager; We don't need to do anything else within the Postgres CLI now that we have the database
created, so let's come out of the CLI by typing \q.
It's important to note, that if you were to modify your models later, then you'll need
to migrate these changes.
Let's go ahead and access the Python interpreter by typing "python3" and enter.
From here, we need to import our 'db' variable found within the taskmanager package, so type:
from taskmanager import db
Now, using db.create_all() method:

"""