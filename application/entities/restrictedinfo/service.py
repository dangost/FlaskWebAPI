from application import db
from typing import List
from .model import RestrictedInfo
from .interface import RestrictedInfoInterface


class RestrictedInfoService:
    def get_all(self) -> List[RestrictedInfo]:
        return RestrictedInfo.query.all()

    def get_by_id(self, restrictedinfo_id: int) -> RestrictedInfo:
        return RestrictedInfo.query.get(restrictedinfo_id)

    def update(self, restrictedinfo: RestrictedInfo, restrictedinfo_change_updates: RestrictedInfoInterface) -> RestrictedInfo:
        restrictedinfo.update(restrictedinfo_change_updates)
        db.session.commit()
        return restrictedinfo

    def delete_by_id(self, restrictedinfo_id: int) -> List[int]:
        restrictedinfo = RestrictedInfo.query.filter(RestrictedInfo.PersonId == restrictedinfo_id).first()
        if not restrictedinfo:
            return []
        db.session.delete(restrictedinfo)
        db.session.commit()
        return [restrictedinfo_id]

    def create(self, new_attrs: RestrictedInfoInterface) -> RestrictedInfo:
        new_restrictedinfo = RestrictedInfo(PersonId=new_attrs["PersonId"],  DateOfBirth=new_attrs["DateOfBirth"],  DateOfDeath=new_attrs["DateOfDeath"],  GovernmentId=new_attrs["GovernmentId"],  PassportId=new_attrs["PassportId"],  HireDire=new_attrs["HireDire"],  SeniorityCode=new_attrs["SeniorityCode"])
        db.session.add(new_restrictedinfo)
        db.session.commit()

        return new_restrictedinfo

