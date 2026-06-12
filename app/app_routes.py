from app import app, db
from flask import render_template, request, session, redirect, url_for, jsonify

from app.secret import secret
from app.warrior_cat import get_cats_by_name, get_cats_by_id
from app.models import WarriorCat

app.secret_key = secret

@app.route("/")
def home():
    return render_template("main.html", title="Home", content="Welcome to warrior cats word games")

@app.route("/warriorcatsdle")
def warriorcatsdle():
    if "guess_cat_ids" in session:
        cats = get_cats_by_id(session["guess_cat_ids"])
    else :
        cats = []
    return render_template("warriorcatsdle.html", title="Warrior Cats Word Games", cats=cats)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error), 404

@app.route("/showcats")
def showcats():
    page = db.paginate(db.select(WarriorCat).order_by(WarriorCat.first_introduced.desc()))
    return render_template("all_cats.html", title="All Cats", cats=page)

@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    guess_name = request.form["cat_name"]
    cats = get_cats_by_name(guess_name)
    # No cat found
    if not cats:
        return render_template(
            "warriorcatsdle.html",
            title="Warrior Cats Word Games",
            cats=get_cats_by_id(session["guess_cat_ids"]),
            error="No cat found with that name"
        )
    # Extract IDs from the guess
    new_ids = [cat.id for cat in cats]

    # Initialize session list if missing
    if "guess_cat_ids" not in session:
        session["guess_cat_ids"] = []

    # Check for duplicates
    for c_id in new_ids:
        if c_id in session["guess_cat_ids"]:
            return render_template(
                "warriorcatsdle.html",
                title="Warrior Cats Word Games",
                cats=get_cats_by_id(session["guess_cat_ids"]),
                error="You already submitted that cat"
            )

    # Add new IDs
    session["guess_cat_ids"] += new_ids

    return redirect(url_for("warriorcatsdle"))

@app.route("/autocomplete")
def autocomplete():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify([])

    # Case-insensitive partial match
    cats = db.session.execute(
        db.select(WarriorCat)
        .where(WarriorCat.character_name.ilike(f"%{query}%"))
        .order_by(WarriorCat.character_name)
        .limit(10)
    ).scalars().all()

    # Return only names
    return jsonify([cat.character_name for cat in cats])