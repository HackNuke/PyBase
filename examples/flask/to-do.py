import traceback

from flask import Flask, redirect, render_template, request

from pybase_db import PyBase

# Documentation
# =============
# • Flask
#   https://flask.palletsprojects.com/en/master/
# • Bootstrap (v5)
#   https://getbootstrap.com/docs/5.0/getting-started/introduction/
# • PyBase
#   https://pybase.netlify.app/docs/v1.0.0.html
app = Flask(__name__)

db = PyBase(database="to-do", db_type="toml")
tasks = []

# local tasks list
# ================
# If the list of tasks in the database doesn't exists,
# we will create it and if it isn't empty, then
# it will be the same when starting the server
if db.fetch("tasks") is None:
    db.insert(content={"tasks": []}, mode="w")
else:
    if len(db.get("tasks")) != 0:
        tasks = db.get("tasks")


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_or_render():
    if request.method == "POST":
        try:
            # Raise error if task is an empty string
            if not request.form.get("task"):
                return "<h1>500 Internal Server Error</h1><p>The task must be longer than 1 character</p>"
            # Pushes the task obtained from the form to the db
            db.push("tasks", request.form.get("task"))
            # Pushes the task obtained from the form to the local tasks
            tasks.append(request.form.get("task"))
            return redirect("/")
        except Exception as err:
            return f"<h1>500 Internal Server Error</h1><p>{err}</p>"
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_or_render():
    if request.method == "POST":
        try:
            # Raise error if new_task is an empty string
            if not request.form.get("new_task"):
                return "<h1>500 Internal Server Error</h1><p>The new task must be longer than 1 character</p>"
            # If the selected task exists in the database
            # then update its value to the new value.
            if db.get(f"tasks.{request.form.get('task')}") is not None:
                db.update(f"tasks.{request.form.get('task')}",
                          request.form.get("new_task"))
            # Search local tasks list for the old value and replace it with the new one.
            for i, _ in enumerate(tasks):
                if tasks[i] == request.form.get("task"):
                    tasks[i] = request.form.get("new_task")
            return redirect("/")
        except Exception as err:
            return f"<h1>500 Internal Server Error</h1><p>{err}</p>"
    else:
        return render_template("edit.html", tasks=tasks)


@app.route("/delete", methods=["GET", "POST"])
def delete_or_render():
    if request.method == "POST":
        try:
            # Obtain through the form checkboxes the tasks to be deleted.
            tasks_to_delete = request.form.to_dict()

            for task in tasks_to_delete.keys():
                if db.get(f"tasks.{task}") is not None:
                    db.delete(f"tasks.{task}")
                    tasks.remove(task)
            return redirect("/")
        except Exception as err:
            print(traceback.print_exc())
            return f"<h1>500 Internal Server Error</h1><p>{err}</p>"
    else:
        return render_template("delete.html", tasks=tasks)


# Restart the Flask server with every change to this script.
# NOTE: use this conditional only in development environment.
if __name__ == "__main__":
    app.run(debug=True)
