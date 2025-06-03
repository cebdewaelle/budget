from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from database import Base

class Transaction (Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    date_transaction = Column(Date)
    payee_id = Column(Integer, ForeignKey('payees.id'))
    sub_category = Column(Integer, ForeignKey('subcategories.id'))
    memo = Column(String)
    outflow = Column(Float)
    inflow = Column(Float)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    committed = Column(Boolean)

