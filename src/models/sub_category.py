from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class SubCategory(Base):
    __tablename__ = 'subcategories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    top_category_id = Column(Integer, ForeignKey('topcategories.id'))

