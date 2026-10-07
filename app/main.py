from fastapi import FastAPI
from app.database import engine , Base
from app import models
from app.routers import customers , factor , product , factor_item

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Shop Management API',
    description='A simple API for managing customers , Factors , and Products.',
    version = '1.0.0'
)

app.include_router(customers.router)
app.include_router(factor.router)
app.include_router(product.router)
app.include_router(factor_item.router)

@app.get('/')
def root():
    return {'message':'welcome to the Shop Management API'}