from sqlalchemy.orm import Session
from app.models import Customer
from app.schemas import CustomerCreate
from app.utils import security
from app.log import log_decorator

#********************Create*****************
@log_decorator
def create_customer(db:Session , newCustomer:CustomerCreate):
    obj = Customer(
        username = newCustomer.username,
        password_hash = security.hash_password(newCustomer.password)
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

#*********************Read****************************

def get_customer_by_id(db:Session , myId:int):
    return db.get(Customer , myId)

def get_customer_by_userName(db:Session , myName:str):
    return db.query(Customer).filter(Customer.username >= myName).all()
                                                    # anyone who his name starts with ali

def get_customers(db:Session):
    return db.query(Customer).all()

#**********************Delete**********************

def delete_customer(db:Session , myId:int):
    obj = db.get(Customer,myId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def delete_all_customers(db:Session):
    delCount = db.query(Customer).delete()
    db.commit()
    return delCount

#************************Update*****************************

def update_customer(db:Session , myId:int,updated_customer:CustomerCreate):
    obj = db.get(Customer,myId)

    if obj:
        obj.username = updated_customer.username
        obj.password_hash = security.hash_password(updated_customer.password)
        db.commit()
        db.refresh(obj)

    return obj

def update_customer_toggle_activate(db:Session , myId:int):
    obj = db.get(Customer,myId)

    if obj:
        obj.is_active = not obj.is_active
        db.commit()
        db.refresh(obj)

    return obj
