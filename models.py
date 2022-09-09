from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import declarative_base
from db import db_engine


Base = declarative_base()

class Item (Base):
    __tablename__ = "row_in_sheet"
    id = Column(Integer,primary_key=True)
    order_num = Column(Integer)
    price_usd = Column(Integer)
    rub_price = Column(Float)
    delivery_data = Column(String)
    def __repr__(self):
        return f"Order Num:{self.order_num},Price USD:{self.price_usd},Delivery Date:{self.delivery_data}"

# For making Migrations Run In CLI - python models.py
if __name__ == "__main__":
    Base.metadata.create_all(db_engine)


