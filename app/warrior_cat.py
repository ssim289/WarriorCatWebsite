from app import db
from app.models import WarriorCat


def get_all_cats():
    all_cats = db.session.execute(db.select(WarriorCat)).scalars()
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

def get_cats_by_name(name):
    cats_with_name = db.session.execute(db.select(WarriorCat).filter_by(character_name=name)).scalars().all()
    return cats_with_name

def get_cats_by_id(param):
    cats_by_id = []
    for cat_id in param:
        print(cat_id)
        cats_by_id.append(db.session.execute(db.select(WarriorCat).filter_by(id=cat_id)).scalar())
    return cats_by_id
