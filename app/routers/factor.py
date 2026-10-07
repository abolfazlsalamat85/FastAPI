from fastapi import APIRouter , HTTPException ,Depends,status
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud as crud 
from app.schemas import FactorCreate , FactorOut , FactorUpdate

router = APIRouter(
    prefix='/factors',
    tags=['Factors']
)

#Create
@router.post('/',response_model=FactorOut)
def create_factor(newFactor:FactorCreate,db:Session=Depends(get_db)):
    return crud.create_factor(db,newFactor)

#Read
@router.get('/Id/{myId}',response_model=FactorOut)
def get_factor_by_id(myId:int,db:Session=Depends(get_db)):
    return  crud.get_factor_by_id(db,myId)

@router.get('/Cid/{myCid}',response_model=list[FactorOut])
def get_factor_by_cid(myCid:int,db:Session=Depends(get_db)):
    Factor = crud.get_factor_by_cid(db,myCid)
    if Factor:
        return Factor
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such Factor with CID => ( {myCid} )')

@router.get('/',response_model=list[FactorOut])
def get_factors(db:Session=Depends(get_db)):
    return crud.get_factors(db)

#Update
@router.put('/Id/{myId}', response_model=FactorOut)
def update_factor(myId: int, data: FactorUpdate, db: Session = Depends(get_db)):
    factor = crud.update_factor(db, myId, data.total)
    if not factor:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No Such Factor with ID => ( {myId} )')
    return factor

#Delete
@router.delete('/')
def del_all_factors( db:Session=Depends(get_db)):
    count = crud.delete_all_factors(db)
    return {'msg':f'{count} Factors have deleted succesfully!'}
    
@router.delete('/{myId}',response_model=FactorOut)
def delete_factor(myId:int , db:Session=Depends(get_db)):
    factor = crud.delete_factor(db,myId)
    if factor:
        return factor
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No Such Factor with ID => ( {myId} )')
