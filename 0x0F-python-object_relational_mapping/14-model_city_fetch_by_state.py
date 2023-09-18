#!/usr/bin/python3
'''
Module to lists all State objects from the database hbtn_0e_6_usa
'''
from sys import argv
from model_city import City
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

    # Query to join State and City tables and fetch required details
    results = session.query(State, City)\
        .filter(State.id == City.state_id)\
        .order_by(City.id).all()

    # Display results
    for state, city in results:
        print(f'{state.name}: ({city.id}) {city.name}')

    # Close the session
    session.close()
