from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("main.html", title="Home", content="Welcome to warrior cats word games")

@app.route("/warriorcatsdle")
def warriorcatsdle():
    return render_template("warriorcatsdle.html", title="Warrior Cats Word Games")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error), 404