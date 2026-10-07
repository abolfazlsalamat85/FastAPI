from sqlalchemy.orm import Session
from app.schemas import Factor_itemCreat, Factor_itemOut,Factor_itemUpdate
from app.log import log_decorator
from sqlalchemy import select, delete,update, func
from app.models import FactorItem, Factor

def recalc_factor_total(db: Session, fid: int):
    total = db.scalar(
        select(func.coalesce(func.sum(FactorItem.total), 0))
        .where(FactorItem.fid == fid)
    )
    factor = db.get(Factor, fid)
    if factor:
        factor.total = total
        db.commit()

# Create
@log_decorator
def create_factor_item(db: Session, newitem: Factor_itemCreat):
    obj = FactorItem(
        fid=newitem.fid,
        pid=newitem.pid,
        no=newitem.no,
        price=newitem.price,
        total=newitem.no * newitem.price,
    )
    db.add(obj)
    db.commit()
    recalc_factor_total(db, obj.fid)
    db.refresh(obj)
    return obj


# Read
@log_decorator
def get_factorItem_by_id(db: Session, myId: int):
    return db.get(FactorItem, myId)


@log_decorator
def get_factorItems_by_fid(db: Session, myFid: int):
    sql = select(FactorItem).where(FactorItem.fid == myFid)
    return db.scalars(sql).all()


@log_decorator
def get_factorItems(db: Session):
    return db.scalars(select(FactorItem)).all()


# Update
@log_decorator
def update_factorItem(db: Session, myId: int, updated: Factor_itemUpdate):
    obj = db.get(FactorItem, myId)
    if obj:
        obj.no = updated.no
        obj.price = updated.price
        obj.total = updated.no * updated.price
        db.commit()
        recalc_factor_total(db, obj.fid)
        db.refresh(obj)
    return obj


# Delete
@log_decorator
def delete_factorItem_by_id(db: Session, myId: int):
    obj = db.get(FactorItem, myId)
    if not obj:
        return None
    fid = obj.fid
    deleted = Factor_itemOut.model_validate(obj)   
    db.delete(obj)
    db.commit()
    recalc_factor_total(db, fid)
    return deleted


@log_decorator
def delete_factorItem_by_fid(db: Session, myFid: int):
    result = db.execute(delete(FactorItem).where(FactorItem.fid == myFid))
    db.commit()
    recalc_factor_total(db, myFid)
    return result.rowcount


@log_decorator
def delete_all_factorItems(db: Session):
    result = db.execute(delete(FactorItem))
    db.execute(update(Factor).values(total=0)) 
    db.commit()
    return result.rowcount

def recalc_all_factor_totals(db: Session):
    ids = db.scalars(select(Factor.id)).all()
    for fid in ids:
        recalc_factor_total(db, fid)
    return len(ids)