#!/usr/bin/python3
'''
State class defination module
'''
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''
    City class that represents a table 'cities' in a MySQL database.

    Attributes
    ----------
    id (Column) : int
        Represents a column of an auto-generated, unique integer.
        It's the primary key.
    name (Column) : str
        Represents a column of a string with a maximum of 128 characters.
        Can't be null.
    state_id (Column): int
        Represents a column of an integer.
        Can't be null and is a foreign key to states.id.
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
