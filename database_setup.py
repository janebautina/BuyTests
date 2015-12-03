import sys
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Orders(Base):
  __tablename__ = 'orders'
  id = Column(Integer, primary_key = True)
  count = Column(Integer)
  name = Column(String(80), nullable = False)
  address = Column(String(80), nullable = False)
  email = Column(String(80), nullable = False)

engine = create_engine('sqlite:///orders.db')
Base.metadata.create_all(engine)