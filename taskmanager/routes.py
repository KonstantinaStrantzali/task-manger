from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("tasks.html")
"""
Whenever we call this function by clicking the navbar link for Categories, it will query
the database and retrieve all records from this table, then sort them by the category name.
"""
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories) #first categories is the name is use
    #in categoires.html template and the second is the variable defined above


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))#grab data
        db.session.add(category)# add data to database
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

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