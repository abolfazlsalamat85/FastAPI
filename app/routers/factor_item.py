from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
import app.crud as crud
from app.schemas import Factor_itemCreat, Factor_itemUpdate, Factor_itemOut

router = APIRouter(
    prefix='/factor_items',
    tags=['Factor_items']
)


# Create
@router.post('/', response_model=Factor_itemOut)
def create_factor_item(newfactor_item: Factor_itemCreat, db: Session = Depends(get_db)):
    return crud.create_factor_item(db, newfactor_item)


# Read
@router.get('/Id/{myId}', response_model=Factor_itemOut)
def get_factor_item_by_id(myId: int, db: Session = Depends(get_db)):
    item = crud.get_factorItem_by_id(db, myId)
    if not item:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No Such factor_item with ID => ( {myId} )')
    return item


@router.get('/Fid/{myFid}', response_model=list[Factor_itemOut])
def get_factor_items_by_fid(myFid: int, db: Session = Depends(get_db)):
    return crud.get_factorItems_by_fid(db, myFid)


@router.get('/', response_model=list[Factor_itemOut])
def get_factor_items(db: Session = Depends(get_db)):
    return crud.get_factorItems(db)


# Update
@router.put('/Id/{myId}', response_model=Factor_itemOut)
def update_factor_item(myId: int, newfactor_item: Factor_itemUpdate, db: Session = Depends(get_db)):
    item = crud.update_factorItem(db, myId, newfactor_item)
    if not item:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No Such factor_item with ID => ( {myId} )')
    return item


# Delete
@router.delete('/')
def del_all_factor_items(db: Session = Depends(get_db)):
    count = crud.delete_all_factorItems(db)
    return {'msg': f'{count} factor_items deleted successfully!'}


@router.delete('/Id/{myId}', response_model=Factor_itemOut)
def delete_factor_item_by_id(myId: int, db: Session = Depends(get_db)):
    item = crud.delete_factorItem_by_id(db, myId)
    if not item:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No Such factor_item with ID => ( {myId} )')
    return item


@router.delete('/Fid/{myFid}')
def delete_factor_items_by_fid(myFid: int, db: Session = Depends(get_db)):
    count = crud.delete_factorItem_by_fid(db, myFid)
    return {'msg': f'{count} factor_items deleted successfully!'}
