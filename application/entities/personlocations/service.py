from application import db
from typing import List
from .model import PersonLocation
from .interface import PersonLocationInterface


class PersonLocationsService:
    def get_all(self) -> List[PersonLocation]:
        return PersonLocation.query.all()

    def get_by_id(self, personlocation_id: int) -> PersonLocation:
        return PersonLocation.query.get(personlocation_id)

    def update(self, personlocation: PersonLocation, personlocation_change_updates: PersonLocationInterface) -> PersonLocation:
        personlocation.update(personlocation_change_updates)
        db.session.commit()
        return personlocation

    def delete_by_id(self, personlocation_id: int) -> List[int]:
        personlocation = PersonLocation.query.filter(PersonLocation.PeoplePersonId == personlocation_id).first()
        if not personlocation:
            return []
        db.session.delete(personlocation)
        db.session.commit()
        return [personlocation_id]

    def create(self, new_attrs: PersonLocationInterface) -> PersonLocation:
        new_personlocation = PersonLocation(PeoplePersonId=new_attrs["PeoplePersonId"],  LocationsLocationsId=new_attrs["LocationsLocationsId"],  SubAddress=new_attrs["SubAddress"],  LocationUsage=new_attrs["LocationUsage"],  Notes=new_attrs["Notes"])
        db.session.add(new_personlocation)
        db.session.commit()

        return new_personlocation

