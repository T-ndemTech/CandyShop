from sqlalchemy import String, LargeBinary, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from configure.database import Base
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]

class Shop(Base):
    __tablename__ = "shop"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(255))
    banner: Mapped[bytes] = mapped_column(LargeBinary)
    logo: Mapped[bytes] = mapped_column(LargeBinary)
    owner: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
