from app import db
from app.models import WarriorCat


def get_cats():
    all_cats = db.session.execute(db.select(WarriorCat))
    return all_cats

def add_cats():
    new_cat = WarriorCat()
    new_cat.character_name = "sebpaw"
    new_cat.clan_name = "forest"
    new_cat.clan_role = "medicine"
    new_cat.eye_colour = "blue"
    new_cat.fur_colour = "green"
    new_cat.first_introduced = "Catching fire"
    db.session.add(new_cat)
    db.session.commit()