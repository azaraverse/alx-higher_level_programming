#!/usr/bin/python3
'''Defines State class
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''Class definition of a State inheriting from an instance of
    Base = declarative_base()
    '''
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
