from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from database import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Float)
    date_balance = Column(Date)
    type_account = Column(String)
    in_budget = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
