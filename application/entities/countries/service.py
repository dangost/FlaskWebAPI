from typing import List

from application import db
from .interface import CountryInterface
from .model import Country


class CountriesService:
    def get_all(self) -> List[Country]:
        return Country.query.all()

    def get_by_id(self, country_id: int) -> Country:
        return Country.query.get(country_id)

    def update(self, country: Country, country_change_updates: CountryInterface) -> Country:
        country.update(country_change_updates)
        db.session.commit()
        return country

    def delete_by_id(self, country_id: int) -> List[int]:
        country = Country.query.filter(Country.CountryId == country_id).first()
        if not country:
            return []
        db.session.delete(country)
        db.session.commit()
        return [country_id]

    def create(self, new_attrs: CountryInterface) -> Country:
        new_country = Country(CountryName=new_attrs["CountryName"], CountryCode=new_attrs["CountryCode"],
                              NatLangCode=new_attrs["NatLangCode"], CurrencyCode=new_attrs["CurrencyCode"])
        db.session.add(new_country)
        db.session.commit()

        return new_country
