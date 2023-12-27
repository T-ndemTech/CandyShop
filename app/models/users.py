from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum
from app.database import Base


class RoleEnum(PyEnum):
    buyer = "buyer"
    business_owner = "business_owner"
    operator = "operator"
    prostitute = "prostitute"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    nickname = Column(String)
    role = Column(Enum(RoleEnum))
    date_joined = Column(DateTime)
    last_login = Column(DateTime)
    password = Column(String)