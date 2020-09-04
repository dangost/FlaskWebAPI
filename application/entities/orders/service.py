from application import db
from typing import List
from .model import Orders
from .interface import OrdersInterface


class OrdersService:
    @staticmethod
    def get_all() -> List[Orders]:
        return Orders.query.all()

    @staticmethod
    def get_by_id(orders_id: int) -> Orders:
        return Orders.query.get(orders_id)

    @staticmethod
    def update(orders: Orders, orders_change_updates: OrdersInterface) -> Orders:
        orders.update(orders_change_updates)
        db.session.commit()
        return orders

    @staticmethod
    def delete_by_id(orders_id: int) -> List[int]:
        orders = Orders.query.filter(Orders.OrderId == orders_id).first()
        if not orders:
            return []
        db.session.delete(orders)
        db.session.commit()
        return [orders_id]

    @staticmethod
    def create(new_attrs: OrdersInterface) -> Orders:
        new_orders = Orders(CustomerId=new_attrs["CustomerId"],  SalesRepId=new_attrs["SalesRepId"],  OrderDate=new_attrs["OrderDate"],  OrderCode=new_attrs["OrderCode"],  OrderStatus=new_attrs["OrderStatus"],  OrderTotal=new_attrs["OrderTotal"],  OrderCurrency=new_attrs["OrderCurrency"],  PromotionCode=new_attrs["PromotionCode"])
        db.session.add(new_orders)
        db.session.commit()

        return new_orders

