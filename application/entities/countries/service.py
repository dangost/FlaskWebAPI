from application import db
from typing import List
from .model import Country
from .interface import CountryInterface


class CountriesService:
    @staticmethod
    def get_all() -> List[Country]:
        return Country.query.all()

    @staticmethod
    def get_by_id(country_id: int) -> Country:
        return Country.query.get(country_id)

    @staticmethod
    def update(country: Country, country_change_updates: CountryInterface) -> Country:
        country.update(country_change_updates)
        db.session.commit()
        return country

    @staticmethod
    def delete_by_id(country_id: int) -> List[int]:
        country = Country.query.filter(Country.CountryId == country_id).first()
        if not country:
            return []
        db.session.delete(country)
        db.session.commit()
        return [country_id]

    @staticmethod
    def create(new_attrs: CountryInterface) -> Country:
        new_country = Country(CountryName=new_attrs["CountryName"], CountryCode=new_attrs["CountryCode"], NatLangCode=new_attrs["NatLangCode"], CurrencyCode=new_attrs["CurrencyCode"])
        db.session.add(new_country)
        db.session.commit()

        return new_country
