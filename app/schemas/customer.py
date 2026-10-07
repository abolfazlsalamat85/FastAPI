from pydantic import BaseModel , ConfigDict

class Customer(BaseModel):
    username : str
    photopath : str

class CustomerCreate(Customer):
    password : str

class CustomerOut(Customer):
    model_config = ConfigDict(from_attributes=True)
    id : int

class PasswordCheck(BaseModel):
    password: str