from sqlalchemy import Column , Integer , String , Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__='customers'

    id = Column(Integer , primary_key=True,index=True)
    username=Column(String,nullable=False)
    password_hash = Column(String , nullable=False)
    is_active = Column(Boolean,default=True)
    photopath = Column(String,default='app/static/NoPic.jpg')

    factors = relationship('Factor',back_populates='customer')