from sqlalchemy import LargeBinary, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from configure.database import Base
from typing import Annotated
from geoalchemy2 import Geometry

intpk = Annotated[int, mapped_column(primary_key=True)]

class Order(Base):
    __tablename__ = "order"

    id: Mapped[intpk]
    location: Mapped[str] = mapped_column(Geometry("POINT"))
    description: Mapped[str] = mapped_column(String)
    photo: Mapped[bytes] = mapped_column(LargeBinary)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    prostitute_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

