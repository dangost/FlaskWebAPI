from application import db
from typing import List
from .model import Orders
from .interface import OrdersInterface


class OrdersService:
    def get_all(self) -> List[Orders]:
        return Orders.query.all()

    def get_by_id(self, orders_id: int) -> Orders:
        return Orders.query.get(orders_id)

    def update(self, orders: Orders, orders_change_updates: OrdersInterface) -> Orders:
        orders.update(orders_change_updates)
        db.session.commit()
        return orders

    def delete_by_id(self, orders_id: int) -> List[int]:
        orders = Orders.query.filter(Orders.OrderId == orders_id).first()
        if not orders:
            return []
        db.session.delete(orders)
        db.session.commit()
        return [orders_id]

    def create(self, new_attrs: OrdersInterface) -> Orders:
        new_orders = Orders(CustomerId=new_attrs["CustomerId"],  SalesRepId=new_attrs["SalesRepId"],  OrderDate=new_attrs["OrderDate"],  OrderCode=new_attrs["OrderCode"],  OrderStatus=new_attrs["OrderStatus"],  OrderTotal=new_attrs["OrderTotal"],  OrderCurrency=new_attrs["OrderCurrency"],  PromotionCode=new_attrs["PromotionCode"])
        db.session.add(new_orders)
        db.session.commit()

        return new_orders

