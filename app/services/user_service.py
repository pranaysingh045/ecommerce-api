
from sqlalchemy.orm import Session
from app.db_queries import user_queries
from app.api.core import security
from app.schemas.user import CreateUser
from app.models import User
from app.api.core import exception
from sqlalchemy.exc import IntegrityError

def list_users(db:Session,limit:int,offset:int):
    return user_queries.list_users(db,limit,offset)

def create_user(db:Session,data:CreateUser)->User:
    try:
        check_email=user_queries.get_user_by_email(db=db,email=data.email.lower())
        if check_email:
            return exception.ConflictError("Email alredy existes")
        user=user_queries.create_user(db=db,email=data.email,has_password=security.hash_password(data.password))
        db.commit()
        
    except IntegrityError:
        db.rollback()
        raise exception.ConflictError("Email alredy existes")

    db.refresh(user)
    return user


