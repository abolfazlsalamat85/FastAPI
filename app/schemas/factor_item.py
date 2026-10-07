from pydantic import BaseModel, ConfigDict

class Factor_item(BaseModel):
    fid: int
    pid: int
    no: int
    price: float

class Factor_itemCreat(Factor_item):
    pass                    

class Factor_itemUpdate(BaseModel):
    no: int
    price: float

class Factor_itemOut(Factor_item):
    id: int
    total: float
    model_config = ConfigDict(from_attributes=True)