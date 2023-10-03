from datetime import datetime

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ProductCreateRequest(ProductBase):
    pass


class InventoryBase(BaseModel):
    id: int
    product_id: int
    quantity: int


class InventoryResponse(InventoryBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    sale_date: datetime

    class Config:
        orm_mode = True

