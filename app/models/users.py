from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from configure.database import Base
from typing import Annotated
import enum

intpk = Annotated[int, mapped_column(primary_key=True)]


class RoleEnum(enum.Enum):
    buyer = "buyer"
    business_owner = "business_owner"
    operator = "operator"
    prostitute = "prostitute"

class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(64), nullable=True)
    role: Mapped[RoleEnum]