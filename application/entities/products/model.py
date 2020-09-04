from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import ProductInterface


class Product(db.Model):

    __tablename__ = "Products"

    ProductId = Column(Integer(), primary_key=True)
    ProductName = Column(String(255))
    Description = Column(String(255))
    Category = Column(Integer())
    WeightClass = Column(String(255))
    WarrantyPeriod = Column(Integer())
    SupplierId = Column(Integer())
    Status = Column(String(255))
    ListPrice = Column(Integer())
    MinimumPrice = Column(Integer())
    PriceCurrency = Column(String(255))
    CatalogURL = Column(String(255))


    def update(self, changes: ProductInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



