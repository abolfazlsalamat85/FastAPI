from sqlalchemy import Column , Integer , String , Boolean , ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class FactorItem(Base):
    __tablename__='factor_items'

    id = Column(Integer , primary_key=True,index=True)
    fid = Column(Integer , ForeignKey('factors.id'))
    pid = Column(Integer , ForeignKey('product.id'))
    no = Column(Integer,default=1)
    price = Column(Integer,default=0)
    total = Column(Integer,default=0)

    factor=relationship('Factor',back_populates='items')
    product=relationship('Product',back_populates='factor_items')
