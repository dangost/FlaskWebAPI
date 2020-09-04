from application import db
from typing import List
from .model import Location
from .interface import LocationInterface


class LocationsService:
    def get_all(self) -> List[Location]:
        return Location.query.all()

    def get_by_id(self, location_id: int) -> Location:
        return Location.query.get(location_id)

    def update(self, location: Location, location_change_updates: LocationInterface) -> Location:
        location.update(location_change_updates)
        db.session.commit()
        return location

    def delete_by_id(self, location_id: int) -> List[int]:
        location = Location.query.filter(Location.LocationId == location_id).first()
        if not location:
            return []
        db.session.delete(location)
        db.session.commit()
        return [location_id]

    def create(self, new_attrs: LocationInterface) -> Location:
        new_location = Location(CountryId=new_attrs["CountryId"],  AddressLine1=new_attrs["AddressLine1"],  AddressLine2=new_attrs["AddressLine2"],  City=new_attrs["City"],  State=new_attrs["State"],  District=new_attrs["District"],  PostalCode=new_attrs["PostalCode"],  LocationTypeCode=new_attrs["LocationTypeCode"],  Description=new_attrs["Description"],  ShippingNotes=new_attrs["ShippingNotes"],  CountriesCountryId=new_attrs["CountriesCountryId"])
        db.session.add(new_location)
        db.session.commit()

        return new_location

