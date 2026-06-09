from app import app, db
from flask import render_template

from app.warrior_cat import get_cats, add_cats
from app.models import WarriorCat


@app.route("/")
def home():
    return render_template("main.html", title="Home", content="Welcome to warrior cats word games")

@app.route("/warriorcatsdle")
def warriorcatsdle():
    cats = get_cats()
    return render_template("warriorcatsdle.html", title="Warrior Cats Word Games", cats=cats)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error), 404

@app.route("/addcats")
def addcats():
    add_cats()
    cat = db.first_or_404(db.select(WarriorCat))
    return render_template("addcats.html", title="Add Cats", cat=cat)