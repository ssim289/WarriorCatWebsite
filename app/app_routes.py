from app import app, db
from flask import render_template

from app.warrior_cat import get_cats
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

@app.route("/showcats")
def showcats():
    page = db.paginate(db.select(WarriorCat).order_by(WarriorCat.first_introduced.desc()))
    return render_template("all_cats.html", title="All Cats", cats=page)