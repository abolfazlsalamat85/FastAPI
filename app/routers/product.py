from fastapi import APIRouter , HTTPException ,Depends,status
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud as crud 
from app.schemas import ProductCreate , ProductOut

router = APIRouter(
    prefix='/products',
    tags=['Products']
)

#Create
@router.post('/',response_model=ProductOut)
def create_product(newproduct:ProductCreate,db:Session=Depends(get_db)):
    return crud.create_Product(db,newproduct)

#Read
@router.get('/Id/{myId}', response_model=ProductOut)
def get_product_by_id(myId: int, db: Session = Depends(get_db)):
    product = crud.get_Product_by_id(db, myId)
    if not product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No Such product with ID => ( {myId} )')
    return product

@router.get('/Name/{myName}',response_model=list[ProductOut])
def get_product_by_name(myName:str,db:Session=Depends(get_db)):
    product = crud.get_Products_by_name(db,myName)
    if product:
        return product
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such product with Name => ( {myName} )')

@router.get('/', response_model=list[ProductOut])
def get_products(name: str | None = None, price: float | None = None, db: Session = Depends(get_db)):
    return crud.search_products(db, name, price)

#Update
@router.put('/{myId}',response_model=ProductOut)
def update_product(myId:int,newProduct:ProductCreate,db:Session=Depends(get_db)):
    product = crud.update_Product(db,myId,newProduct)
    if product:
        return product
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such product with ID => ( {myId} )')

#Delete
@router.delete('/')
def del_all_products( db:Session=Depends(get_db)):
    count = crud.delete_all_Products(db)
    return {'msg':f'{count} products have deleted succesfully!'}
    
@router.delete('/{myId}',response_model=ProductOut)
def delete_product(myId:int , db:Session=Depends(get_db)):
    product = crud.delete_Product_by_id(db,myId)
    if product:
        return product
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such product with ID => ( {myId} )')
