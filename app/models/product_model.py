from sqlalchemy import Column , Integer , String , Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__='product'

    id = Column(Integer , primary_key=True,index=True)
    name=Column(String,nullable=False)
    price = Column(Integer,default=0)

    factor_items = relationship('FactorItem',back_populates='product')
 