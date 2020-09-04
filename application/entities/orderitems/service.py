from application import db
from typing import List
from .model import OrderItem
from .interface import OrderItemInterface


class OrderItemsService:
    @staticmethod
    def get_all() -> List[OrderItem]:
        return OrderItem.query.all()

    @staticmethod
    def get_by_id(orderitem_id: int) -> OrderItem:
        return OrderItem.query.get(orderitem_id)

    @staticmethod
    def update(orderitem: OrderItem, orderitem_change_updates: OrderItemInterface) -> OrderItem:
        orderitem.update(orderitem_change_updates)
        db.session.commit()
        return orderitem

    @staticmethod
    def delete_by_id(orderitem_id: int) -> List[int]:
        orderitem = OrderItem.query.filter(OrderItem.OrderItemId == orderitem_id).first()
        if not orderitem:
            return []
        db.session.delete(orderitem)
        db.session.commit()
        return [orderitem_id]

    @staticmethod
    def create(new_attrs: OrderItemInterface) -> OrderItem:
        new_orderitem = OrderItem(OrderId=new_attrs["OrderId"],  ProductId=new_attrs["ProductId"],  UnitPrice=new_attrs["UnitPrice"],  Quantity=new_attrs["Quantity"])
        db.session.add(new_orderitem)
        db.session.commit()

        return new_orderitem

