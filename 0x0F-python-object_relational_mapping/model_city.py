#!/usr/bin/python3
"""the class definition of a city and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """class state"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
