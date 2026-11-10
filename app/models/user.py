from sqlalchemy import String,func
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.product import Product


class User(Base):
    __tablename__= "users"

    id: Mapped[int]=mapped_column(primary_key=True)
    email: Mapped[str]=mapped_column(String(255),unique=True,index=True)
    hashed_password: Mapped[str]=mapped_column(String(256))
    role: Mapped[str]=mapped_column(default="customer",type_=String(20))
    is_active:Mapped[bool]=mapped_column(default=True)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())

    products: Mapped[list["Product"]] = relationship(back_populates="seller")

    