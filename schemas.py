# app/schemas.py

from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    stock: int
    category: str
    description: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
