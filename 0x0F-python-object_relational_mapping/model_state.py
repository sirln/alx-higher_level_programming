#!/usr/bin/python3
'''
State class defination module
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    State class that represents a table 'states' in a MySQL database.

    Attributes
    ----------
    id (Column) : int
        Represents a column of an auto-generated, unique integer.
        It's the primary key.
    name (Column) : str
        Represents a column of a string with a maximum of 128 characters.
        Can't be null.
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
