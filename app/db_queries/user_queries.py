from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User



def list_users(db:Session,limit:int,offset:int) ->list[User]:
    stmt=select(User).order_by(User.id).limit(limit=limit).offset(offset=offset)
    # stmt = select(User).order_by(User.id).limit(limit).offset(offset)
    return list(db.scalars(stmt).all())

def get_user_by_email(db:Session,email:str):
    stmt=select(User).where(User.email==email)
    return db.scalar(stmt)

def get_user_by_id(db:Session,id:int):
    q=select(User).where(User.id==id)
    return db.scalar(q)

def create_user(db:Session,email:str,has_password:str)->User:
    q=User(email=email,hashed_password=has_password)
    db.add(q)
    db.flush() #only send request get id but not commit yet
    return q




