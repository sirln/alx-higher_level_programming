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

    # Connectivity to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query and print State objects with letter `a`
    a_states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)

    # Looping throught the results
    for a_state in a_states:
        print(f'{a_state.id}: {a_state.name}')

    # Close the session
    session.close()
