from sqlalchemy import Column , Integer , String , Boolean , ForeignKey , DateTime
from datetime import datetime
from jdatetime import date as jdate
from sqlalchemy.orm import relationship
from app.database import Base

class Factor(Base):
    __tablename__='factors'

    id = Column(Integer , primary_key=True,index=True)
    cid = Column(Integer , ForeignKey('customers.id'))
    date=Column(DateTime,default=datetime.now)
    total = Column(Integer,default=0)
    jdate = Column(String,default='')

    customer = relationship('Customer',back_populates='factors')
    items = relationship('FactorItem',back_populates='factor')
