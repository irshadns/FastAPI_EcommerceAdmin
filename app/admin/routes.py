from typing import List

from fastapi import APIRouter, status

from app.admin.schemas import ProductResponse, ProductCreateRequest, SaleResponse, InventoryResponse
from app.config import PAGINATION_LIMIT
from app.core.auth import get_unauthorized_response, admin_dependency
from app.database import db_dependency
from app.ecommerce.models import Product, Sale, Inventory

router = APIRouter(
    prefix='/admin',
    tags=['Admin Dashboard']
)


@router.get("/sales/", status_code=status.HTTP_200_OK)
def get_sales(user: admin_dependency, db: db_dependency):
    if not user:
        raise get_unauthorized_response()
    return "SALES DATA"


@router.get("/products/", status_code=status.HTTP_200_OK, response_model=List[ProductResponse])
def get_products(user: admin_dependency, db: db_dependency, skip: int = 0, limit: int = PAGINATION_LIMIT):
    return db.query(Product).offset(skip).limit(limit).all()


@router.post("/products/", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
def create_product(user: admin_dependency, product: ProductCreateRequest, db: db_dependency):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/sales/", status_code=status.HTTP_200_OK, response_model=List[SaleResponse])
def get_sales(user: admin_dependency, db: db_dependency, skip: int = 0, limit: int = PAGINATION_LIMIT):
    return db.query(Sale).offset(skip).limit(limit).all()


@router.get("/inventory/", status_code=status.HTTP_200_OK, response_model=List[InventoryResponse])
def get_inventory(user: admin_dependency, db: db_dependency, skip: int = 0, limit: int = PAGINATION_LIMIT):
    return db.query(Inventory).offset(skip).limit(limit).all()
