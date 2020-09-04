from application import db
from typing import List
from .model import Product
from .interface import ProductInterface


class ProductsService:
    @staticmethod
    def get_all() -> List[Product]:
        return Product.query.all()

    @staticmethod
    def get_by_id(product_id: int) -> Product:
        return Product.query.get(product_id)

    @staticmethod
    def update(product: Product, product_change_updates: ProductInterface) -> Product:
        product.update(product_change_updates)
        db.session.commit()
        return product

    @staticmethod
    def delete_by_id(product_id: int) -> List[int]:
        product = Product.query.filter(Product.ProductId == product_id).first()
        if not product:
            return []
        db.session.delete(product)
        db.session.commit()
        return [product_id]

    @staticmethod
    def create(new_attrs: ProductInterface) -> Product:
        new_product = Product(ProductName=new_attrs["ProductName"],  Description=new_attrs["Description"],  Category=new_attrs["Category"],  WeightClass=new_attrs["WeightClass"],  WarrantyPeriod=new_attrs["WarrantyPeriod"],  SupplierId=new_attrs["SupplierId"],  Status=new_attrs["Status"],  ListPrice=new_attrs["ListPrice"],  MinimumPrice=new_attrs["MinimumPrice"],  PriceCurrency=new_attrs["PriceCurrency"],  CatalogURL=new_attrs["CatalogURL"])
        db.session.add(new_product)
        db.session.commit()

        return new_product

