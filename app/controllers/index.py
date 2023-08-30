from flask import render_template
from app import app


@app.route("/index/<user>")
@app.route("/<user>")
@app.route("/", defaults={'user':None})
def index(user):
    if user:
        return render_template('index.html', user=user)
    else:
        user = ""
    return render_template('index.html', user=user)