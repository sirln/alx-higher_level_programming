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

    # Create a new State object for `Louisiana`
    new_state = State(name='Louisiana')

    # Connectivity to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query the State object with name with `a`
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%')).all()

    # Delete each state that matches the condition
    for state in states_to_delete:
        session.delete(state)

    session.commit()

    # Close the session
    session.close()
