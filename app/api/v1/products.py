from fastapi import APIRouter

router=APIRouter(prefix="/products",tags=["Product"])

@router.get("/list")
def get():
    return "this is first fun"