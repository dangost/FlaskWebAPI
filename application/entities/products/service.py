from typing import List

from application import db
from .interface import ProductInterface
from .model import Product


class ProductsService:
    def get_all(self) -> List[Product]:
        return Product.query.all()

    def get_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)

    def update(self, product: Product, product_change_updates: ProductInterface) -> Product:
        product.update(product_change_updates)
        db.session.commit()
        return product

    def delete_by_id(self, product_id: int) -> List[int]:
        product = Product.query.filter(Product.ProductId == product_id).first()
        if not product:
            return []
        db.session.delete(product)
        db.session.commit()
        return [product_id]

    def create(self, new_attrs: ProductInterface) -> Product:
        new_product = Product(ProductName=new_attrs["ProductName"], Description=new_attrs["Description"],
                              Category=new_attrs["Category"], WeightClass=new_attrs["WeightClass"],
                              WarrantyPeriod=new_attrs["WarrantyPeriod"], SupplierId=new_attrs["SupplierId"],
                              Status=new_attrs["Status"], ListPrice=new_attrs["ListPrice"],
                              MinimumPrice=new_attrs["MinimumPrice"], PriceCurrency=new_attrs["PriceCurrency"],
                              CatalogURL=new_attrs["CatalogURL"])
        db.session.add(new_product)
        db.session.commit()

        return new_product
