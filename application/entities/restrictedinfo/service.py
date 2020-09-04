from application import db
from typing import List
from .model import RestrictedInfo
from .interface import RestrictedInfoInterface


class RestrictedInfoService:
    @staticmethod
    def get_all() -> List[RestrictedInfo]:
        return RestrictedInfo.query.all()

    @staticmethod
    def get_by_id(restrictedinfo_id: int) -> RestrictedInfo:
        return RestrictedInfo.query.get(restrictedinfo_id)

    @staticmethod
    def update(restrictedinfo: RestrictedInfo, restrictedinfo_change_updates: RestrictedInfoInterface) -> RestrictedInfo:
        restrictedinfo.update(restrictedinfo_change_updates)
        db.session.commit()
        return restrictedinfo

    @staticmethod
    def delete_by_id(restrictedinfo_id: int) -> List[int]:
        restrictedinfo = RestrictedInfo.query.filter(RestrictedInfo. == restrictedinfo_id).first()
        if not restrictedinfo:
            return []
        db.session.delete(restrictedinfo)
        db.session.commit()
        return [restrictedinfo_id]

    @staticmethod
    def create(new_attrs: RestrictedInfoInterface) -> RestrictedInfo:
        new_restrictedinfo = RestrictedInfo(DateOfBirth=new_attrs["DateOfBirth"],  DateOfDeath=new_attrs["DateOfDeath"],  GovernmentId=new_attrs["GovernmentId"],  PassportId=new_attrs["PassportId"],  HireDire=new_attrs["HireDire"],  SeniorityCode=new_attrs["SeniorityCode"])
        db.session.add(new_restrictedinfo)
        db.session.commit()

        return new_restrictedinfo

