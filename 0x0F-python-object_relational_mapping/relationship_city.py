#!/usr/bin/python3
"""file that contains the class relationship of a City with State"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Define State class"""
    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
