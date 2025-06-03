from sqlalchemy import Column, Integer, String
from database import Base


class Payee(Base):
    __tablename__ = 'payees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
