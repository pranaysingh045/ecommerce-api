from fastapi import APIRouter,Query,Depends,status
from app.schemas.user import UserRead,CreateUser
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import user_service


router=APIRouter(tags=["Users"],prefix='/user')

@router.post('/register',response_model=UserRead,status_code=status.HTTP_201_CREATED)
def create_user(data:CreateUser,db:Session=Depends(get_db)):
    return user_service.create_user(db=db,data=data)

@router.get('/',response_model=list[UserRead])
def list_user(
    limit:int=Query(20,ge=1,le=100),
    offset:int=Query(0,ge=0),
    db:Session=Depends(get_db),
    )->UserRead:

    return user_service.list_users(db,limit,offset)


