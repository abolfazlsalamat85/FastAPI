from fastapi import APIRouter , HTTPException ,Depends,status
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud as crud 
from app.schemas import CustomerCreate , CustomerOut , PasswordCheck
from app.utils import security

router = APIRouter(
    prefix='/customers',
    tags=['Customers']
)

#Create
@router.post('/',response_model=CustomerOut)
def create_customer(customer:CustomerCreate,db:Session=Depends(get_db)):
    for item in customer:
        print(item)
    new_customer=crud.create_customer(db,customer)
    return new_customer

#Read
@router.get('/',response_model=list[CustomerOut])
def get_customers(db:Session=Depends(get_db)):
    return  crud.get_customers(db)

@router.post('/VerifyId/{myId}')
def verify_customer_password(myId: int, password: PasswordCheck, db: Session = Depends(get_db)):
    customer = crud.get_customer_by_id(db, myId)
    if not customer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No Such Customer with ID => ( {myId} )')
    return {'valid': security.verify_password(password.password, customer.password_hash)}

@router.get('/Id/{myId}',response_model=CustomerOut)
def get_customer_by_id(myId:int,db:Session=Depends(get_db)):
    customer = crud.get_customer_by_id(db,myId)
    if customer:
        return customer
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such Customer with ID => ( {myId} )')

@router.get('/{myUsername}',response_model=list[CustomerOut])
def get_customer_by_id(myUsername:str,db:Session=Depends(get_db)):
    return crud.get_customer_by_userName(db,myUsername)

#Update
@router.put('/',response_model=CustomerOut)
def update_customer(myId:int,incustomer : CustomerCreate,db:Session=Depends(get_db)):
    customer = crud.update_customer(db,myId,incustomer)
    if customer:
        return customer
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such Customer with ID => ( {myId} )')
    
@router.put('/{myId}',response_model=CustomerOut)
def update_customer_toggle_activate(myId:int , db:Session=Depends(get_db)):
    customer = crud.update_customer_toggle_activate(db,myId)
    if customer:
        return customer
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such Customer with ID => ( {myId} )')

#Delete
@router.delete('/')
def del_all_customers( db:Session=Depends(get_db)):
    count = crud.delete_all_customers(db)
    return {'msg':f'{count} customers have deleted succesfully!'}
    
@router.delete('/{myId}',response_model=CustomerOut)
def delete_customer(myId:int , db:Session=Depends(get_db)):
    customer = crud.delete_customer(db,myId)
    if customer:
        return customer
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such Customer with ID => ( {myId} )')
