from application import db
from typing import List
from .model import PhoneNumber
from .interface import PhoneNumberInterface


class PhoneNumbersService:
    @staticmethod
    def get_all() -> List[PhoneNumber]:
        return PhoneNumber.query.all()

    @staticmethod
    def get_by_id(phonenumber_id: int) -> PhoneNumber:
        return PhoneNumber.query.get(phonenumber_id)

    @staticmethod
    def update(phonenumber: PhoneNumber, phonenumber_change_updates: PhoneNumberInterface) -> PhoneNumber:
        phonenumber.update(phonenumber_change_updates)
        db.session.commit()
        return phonenumber

    @staticmethod
    def delete_by_id(phonenumber_id: int) -> List[int]:
        phonenumber = PhoneNumber.query.filter(PhoneNumber.PhoneNumberId == phonenumber_id).first()
        if not phonenumber:
            return []
        db.session.delete(phonenumber)
        db.session.commit()
        return [phonenumber_id]

    @staticmethod
    def create(new_attrs: PhoneNumberInterface) -> PhoneNumber:
        new_phonenumber = PhoneNumber(PeoplePersonId=new_attrs["PeoplePersonId"],  LocationLocationId=new_attrs["LocationLocationId"],  Phonenumber=new_attrs["Phonenumber"],  CountryCode=new_attrs["CountryCode"],  PhoneType=new_attrs["PhoneType"])
        db.session.add(new_phonenumber)
        db.session.commit()

        return new_phonenumber

