from sqlalchemy import String, LargeBinary, ForeignKey, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from configure.database import Base
from typing import Annotated
import enum

class Type(enum.Enum):
    whore = "whore"
    drug = "drug"


intpk = Annotated[int, mapped_column(primary_key=True)]

class Product(Base):
    __tablename__ = "product"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[int]
    type: Mapped[Type]
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    count_in_stock: Mapped[int]
    salesman: Mapped[int] = mapped_column(ForeignKey("shop.id", ondelete="CASCADE"))
