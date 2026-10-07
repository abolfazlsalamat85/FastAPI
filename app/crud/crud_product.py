from sqlalchemy.orm import Session
from sqlalchemy import select , delete
from app.models import Product
from app.schemas import ProductCreate
from app.log import log_decorator

@log_decorator
def create_Product(db:Session , newProduct:ProductCreate):
    obj = Product(
        name = newProduct.name,
        price = newProduct.price
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
#Read
@log_decorator
def search_products(db: Session, name: str | None = None, price: float | None = None):
    sql = select(Product)
    if name:
        sql = sql.where(Product.name.ilike(f"%{name.strip()}%"))
    if price is not None:
        sql = sql.where(Product.price == price)
    return db.scalars(sql.order_by(Product.name)).all()

@log_decorator
def get_Product_by_id(db:Session , myId:int):
    return db.get(Product,myId)
@log_decorator
def get_Products_by_name(db:Session,myName:int):
    sql = (
        select(Product)
        .where(Product.name.ilike(f"%{myName.strip()}%"))
        .order_by(Product.name)
    )
    return db.scalars(sql).all()
@log_decorator    
def get_Products_by_price(db:Session,myPrice:int):
    return db.query(Product).filter(Product.price == myPrice).all()
@log_decorator
def get_Products(db:Session):
    # return db.query(Product).order_by(Product.name).all()
    sql = select(Product).order_by(Product.name)
    return db.scalars(sql).all()



#Delete
@log_decorator
def delete_Product_by_id(db:Session , MyId:int):
    obj = db.get(Product,MyId)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

@log_decorator
def delete_all_Products(db:Session):
    delCount = db.query(Product).delete()
    db.commit()
    return delCount
@log_decorator
def update_Product(db:Session , myId:int, updated_Product:ProductCreate):
    obj = db.get(Product, myId)
    if obj:
        obj.name = updated_Product.name
        obj.price = updated_Product.price
        db.commit()
        db.refresh(obj)
    return obj