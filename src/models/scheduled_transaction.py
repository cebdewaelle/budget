from sqlalchemy import CheckConstraint, Column, Integer, String, Float, Date, ForeignKey
from database import Base

FREQUENCIES = ('Unique', 'Quotidien', 'Bihebdomadaire', 'Hebdomadaire', 'Bimensuel ', 'Quadrihebdomadaire',
               'Mensuel', 'Bimestriel', 'Trimestriel', 'Quadrimestriel', 'Semestriel', 'Annuel', 'Bisannuel')

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
    frequency = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint(f"frequency IN {FREQUENCIES}", name="check_frequency"),
    )
