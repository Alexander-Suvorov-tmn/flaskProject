from sqlalchemy import Column, Integer, DateTime, BigInteger, Float
from .connected import Base

from dateutil.parser import parse


class OrderData(Base):
    __tablename__ = 'order_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order = Column(BigInteger, index=True, unique=True)
    price = Column(BigInteger, index=True)
    price_rus = Column(Float, index=True)
    delivery_time = Column(DateTime)

    __mapper_args__ = {"eager_defaults": True}
    
    def __init__(self, id, order, price, price_rus, delivery_time):
        self.id = id
        self.order = order
        self.price = price
        self.price_rus = price_rus
        self.delivery_time = delivery_time
        

    def __repr__(self):
            return (
                f"<{self.__class__.__name__}("
                f"id={self.id}, "
                f"order={self.order}, "
                f"delivery_time={self.delivery_time}"
                f")>"
            )
            
            
    def json(self):
        return {
            "id":self.id, 
            "order":self.order, 
            "price":self.price, 
            "price_rus":self.price_rus,
            "delivery_time":parse(self.delivery_time).date()
            }
