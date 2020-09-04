from application import db
from typing import List
from .model import Location
from .interface import LocationInterface


class LocationsService:
    @staticmethod
    def get_all() -> List[Location]:
        return Location.query.all()

    @staticmethod
    def get_by_id(location_id: int) -> Location:
        return Location.query.get(location_id)

    @staticmethod
    def update(location: Location, location_change_updates: LocationInterface) -> Location:
        location.update(location_change_updates)
        db.session.commit()
        return location

    @staticmethod
    def delete_by_id(location_id: int) -> List[int]:
        location = Location.query.filter(Location.LocationId == location_id).first()
        if not location:
            return []
        db.session.delete(location)
        db.session.commit()
        return [location_id]

    @staticmethod
    def create(new_attrs: LocationInterface) -> Location:
        new_location = Location(CountryId=new_attrs["CountryId"],  AdressLine1=new_attrs["AdressLine1"],  AdressLine2=new_attrs["AdressLine2"],  City=new_attrs["City"],  State=new_attrs["State"],  District=new_attrs["District"],  PostalCode=new_attrs["PostalCode"],  LocationTypeCode=new_attrs["LocationTypeCode"],  Description=new_attrs["Description"],  ShippingNotes=new_attrs["ShippingNotes"],  CountriesCountryId=new_attrs["CountriesCountryId"])
        db.session.add(new_location)
        db.session.commit()

        return new_location

