from application import db
from typing import List
from .model import Person
from .interface import PersonInterface


class PeopleService:
    @staticmethod
    def get_all() -> List[Person]:
        return Person.query.all()

    @staticmethod
    def get_by_id(person_id: int) -> Person:
        return Person.query.get(person_id)

    @staticmethod
    def update(person: Person, person_change_updates: PersonInterface) -> Person:
        person.update(person_change_updates)
        db.session.commit()
        return person

    @staticmethod
    def delete_by_id(person_id: int) -> List[int]:
        person = Person.query.filter(Person.Id == person_id).first()
        if not person:
            return []
        db.session.delete(person)
        db.session.commit()
        return [person_id]

    @staticmethod
    def create(new_attrs: PersonInterface) -> Person:
        new_person = Person(FirstName=new_attrs["FirstName"],  LastName=new_attrs["LastName"],  MiddleName=new_attrs["MiddleName"],  Nickname=new_attrs["Nickname"],  NatLangCode=new_attrs["NatLangCode"],  CultureCode=new_attrs["CultureCode"],  Gender=new_attrs["Gender"])
        db.session.add(new_person)
        db.session.commit()

        return new_person

