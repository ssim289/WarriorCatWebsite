from sqlalchemy.orm import Mapped, mapped_column
from app import db, app


class WarriorCat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str]
    clan_role: Mapped[str]
    clan_name: Mapped[str]
    eye_colour: Mapped[str]
    fur_colour: Mapped[str]
    first_introduced: Mapped[str]

with app.app_context():
    db.create_all()
