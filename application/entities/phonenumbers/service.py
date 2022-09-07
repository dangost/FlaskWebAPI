from typing import List

from application import db
from .interface import PhoneNumberInterface
from .model import PhoneNumber


class PhoneNumbersService:
    def get_all(self) -> List[PhoneNumber]:
        return PhoneNumber.query.all()

    def get_by_id(self, phonenumber_id: int) -> PhoneNumber:
        return PhoneNumber.query.get(phonenumber_id)

    def update(self, phonenumber: PhoneNumber, phonenumber_change_updates: PhoneNumberInterface) -> PhoneNumber:
        phonenumber.update(phonenumber_change_updates)
        db.session.commit()
        return phonenumber

    def delete_by_id(self, phonenumber_id: int) -> List[int]:
        phonenumber = PhoneNumber.query.filter(PhoneNumber.PhoneNumberId == phonenumber_id).first()
        if not phonenumber:
            return []
        db.session.delete(phonenumber)
        db.session.commit()
        return [phonenumber_id]

    def create(self, new_attrs: PhoneNumberInterface) -> PhoneNumber:
        new_phonenumber = PhoneNumber(PeoplePersonId=new_attrs["PeoplePersonId"],
                                      LocationLocationId=new_attrs["LocationLocationId"],
                                      PhoneNumber=new_attrs["PhoneNumber"], CountryCode=new_attrs["CountryCode"],
                                      PhoneType=new_attrs["PhoneType"])
        db.session.add(new_phonenumber)
        db.session.commit()

        return new_phonenumber
