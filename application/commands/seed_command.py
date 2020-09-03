from flask_script import Command

from application import db
from application.entities.countries import Country



def seed_things():
    classes = [Country]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {"name": "Pizza Slicer", "purpose": "Cut delicious pizza"},
        {"name": "Rolling Pin", "purpose": "Roll delicious pizza"},
        {"name": "Pizza Oven", "purpose": "Bake delicious pizza"},
    ]
    db.session.bulk_insert_mappings(cls, things)


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if (
            input(
                "Are you sure you want to drop all tables and recreate? (Y/N)\n"
            ).lower()
            == "y"
        ):
            print("Dropping tables...")
            db.drop_all()
            db.create_all()
            seed_things()

            for each in db.session:
                db.session.remove(each)

            db.session.commit()
            print("DB successfully seeded.")
