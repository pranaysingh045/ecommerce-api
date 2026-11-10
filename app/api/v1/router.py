from fastapi import APIRouter
from app.api.v1 import products,user

api_router=APIRouter()
api_router.include_router(products.router)
api_router.include_router(user.router)
