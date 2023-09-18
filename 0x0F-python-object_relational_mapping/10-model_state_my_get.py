#!/usr/bin/python3
'''
Module to lists all State objects from the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # Connectivity to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query and print State objects with letter name in argument
    state = session.query(State)\
        .filter_by(name=state_name)\
        .first()

    if state:
        print(state.id)
    else:
        print('Not found')

    # Close the session
    session.close()
