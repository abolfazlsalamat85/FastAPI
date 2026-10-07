from pydantic import BaseModel , ConfigDict
from datetime import datetime
from .factor_item import Factor_itemOut

class FactorBase(BaseModel):
    cid :  int
    
class FactorUpdate(BaseModel):
    total: float

class FactorCreate(FactorBase):
    pass
    
class FactorOut(FactorBase):
    model_config = ConfigDict(from_attributes=True)
    id :  int 
    date: datetime
    total :  float
    jdate :  str
    items : list[Factor_itemOut] = []
