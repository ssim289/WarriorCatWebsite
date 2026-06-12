from sqlalchemy.exc import OperationalError

from . import app, db
from app.models import WarriorCat
from .warrior_cat import add_cats

CATS = [
    {
        "character_name": "sebpaw",
        "clan_name": "forest",
        "clan_role" : "medicine",
        "eye_colour": "blue",
        "fur_colour" : "green",
        "first_introduced" : "Catching fire"
    }
]

def get_data_from_db(model):
    try:
        data = db.session.execute(db.select(model))
        db.session.close()
        return data
    except OperationalError:
        return []


def create_database(cat_database):
    cat_database.create_all()
    for data in CATS:
        new_cat = WarriorCat(character_name=data["character_name"],
                             clan_name=data["clan_name"],
                             clan_role=data["clan_role"],
                             eye_colour=data["eye_colour"],
                             fur_colour=data["fur_colour"],
                             first_introduced=data["first_introduced"])
        cat_database.session.add(new_cat)
    cat_database.session.commit()
    print("Created new database")

def update_database(db, existing_cats):
    db.drop_all()
    db.create_all()
    for cat in existing_cats:
        db.session.merge(cat)
    add_cats() #TODO remove this once I fix the initialise of the database.
    db.session.commit()
    print("Updated existing database")


with app.app_context():
    existing_cats = get_data_from_db(WarriorCat)

    if not existing_cats:
        create_database(db)
    else:
        update_database(db, existing_cats)