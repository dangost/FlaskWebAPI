from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import ProductInterface


class Product(db.Model):

    __tablename__ = "Products"

    ProductName = Column(Integer())
    Description = Column(Integer())
    Category = Column(String(255))
    WeightClass = Column(Integer())
    WarrantlyPeriod = Column(String(255))
    SupplierId = Column(String(255))
    Status = Column(Integer())
    ListPrice = Column(String(255))
    MinimumPrice = Column(String(255))
    PriceCurrency = Column(Integer())
    CatalogURL = Column(Integer())


    def update(self, changes: ProductInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



