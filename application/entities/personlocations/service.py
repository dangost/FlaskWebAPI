from application import db
from typing import List
from .model import PersonLocation
from .interface import PersonLocationInterface


class PersonLocationsService:
    @staticmethod
    def get_all() -> List[PersonLocation]:
        return PersonLocation.query.all()

    @staticmethod
    def get_by_id(personlocation_id: int) -> PersonLocation:
        return PersonLocation.query.get(personlocation_id)

    @staticmethod
    def update(personlocation: PersonLocation, personlocation_change_updates: PersonLocationInterface) -> PersonLocation:
        personlocation.update(personlocation_change_updates)
        db.session.commit()
        return personlocation

    @staticmethod
    def delete_by_id(personlocation_id: int) -> List[int]:
        personlocation = PersonLocation.query.filter(PersonLocation. == personlocation_id).first()
        if not personlocation:
            return []
        db.session.delete(personlocation)
        db.session.commit()
        return [personlocation_id]

    @staticmethod
    def create(new_attrs: PersonLocationInterface) -> PersonLocation:
        new_personlocation = PersonLocation(LocationsLocationsId=new_attrs["LocationsLocationsId"],  SubAdress=new_attrs["SubAdress"],  LocationUsage=new_attrs["LocationUsage"],  Notes=new_attrs["Notes"])
        db.session.add(new_personlocation)
        db.session.commit()

        return new_personlocation

