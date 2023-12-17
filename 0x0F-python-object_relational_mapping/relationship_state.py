#!/usr/bin/python3
"""file that contains the class relationship of a State with City"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Define State class"""
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
