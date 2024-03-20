#!/usr/bin/python3
'''Defines City class
'''
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''Class definition of a City inheriting Base of model_state
    '''
    __tablename__ = 'cities'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
