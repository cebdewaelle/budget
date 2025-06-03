from sqlalchemy import Column, Integer, String
from database import Base


class SubCategory(Base):
    __tablename__ = 'topcategories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
