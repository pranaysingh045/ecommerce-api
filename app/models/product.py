from decimal import Decimal

from sqlalchemy import String, Text, func, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import datetime
from app.db.base import Base
from app.models.user import User

# description, price (Numeric 10,2),
#   stock (int, CHECK stock >= 0), is_active, created_at

class Product(Base):
    __tablename__="products"
    __table_args__ = (CheckConstraint("stock >= 0", name="ck_products_stock_nonneg"),)

    id:Mapped[int]=mapped_column(primary_key=True)
    seller_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True)
    category_id:Mapped[int]=mapped_column(ForeignKey("categories.id"),index=True)
    name:Mapped[str]=mapped_column(String(200),index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock:Mapped[int]=mapped_column(default=0)
    is_active:Mapped[bool]=mapped_column(default=True)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())

    seller:Mapped["User"]=relationship(back_populates="products")
    category:Mapped["Category"]=relationship(back_populates="products")



class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))  # null = top level

    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    order: Mapped["Order"] = relationship(back_populates="items")
    product: Mapped["Product"] = relationship()



from sqlalchemy import UniqueConstraint


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    items: Mapped[list["CartItem"]] = relationship(
        back_populates="cart", cascade="all, delete-orphan"
    )


class CartItem(Base):
    __tablename__ = "cart_items"
    __table_args__ = (UniqueConstraint("cart_id", "product_id", name="uq_cart_product"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"), index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(default=1)

    cart: Mapped["Cart"] = relationship(back_populates="items")
