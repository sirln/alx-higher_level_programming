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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # If the state with id = 2 exists, update its name
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
