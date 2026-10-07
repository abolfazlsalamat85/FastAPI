from sqlalchemy.orm import Session
from app.models import Factor
from app.schemas import FactorCreate
from app.utils import date_converter
from app.log import log_decorator


#********************Create*****************

@log_decorator
def create_factor(db:Session , newFactor:FactorCreate):
    obj = Factor(
        cid = newFactor.cid,
        total = 0,
        jdate = date_converter.jalaliToday()
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

#*********************Read****************************
@log_decorator
def get_factor_by_id(db:Session , myId:int):
    return db.get(Factor , myId)
@log_decorator
def get_factor_by_cid(db:Session , myCid:int):
    return db.query(Factor).filter(Factor.cid == myCid).all()
                                                    # anyone who his name starts with ali
@log_decorator
def get_factors(db:Session):
    return db.query(Factor).all()

#**********************Delete**********************
@log_decorator
def delete_factor(db:Session , myId:int):
    obj = db.get(Factor,myId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
@log_decorator
def delete_all_factors(db:Session):
    delCount = db.query(Factor).delete()
    db.commit()
    return delCount

#************************Update*****************************
@log_decorator
def update_factor(db:Session , myId:int,total=float):
    obj = db.get(Factor,myId)

    if obj:
        obj.total = total
        db.commit()
        db.refresh(obj)

    return obj
