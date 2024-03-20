#!/usr/bin/python3
'''A script that lists all city objects from a database
'''
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_city_and_state(username, password, database):
    '''lists all city objects from a database

    Args:
        username (str): username of database user
        password (str): password of database user
        database (str): name of database
    '''

    # define connection url
    db_url = (
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    # create engine
    engine = create_engine(db_url)

    # create all tables
    Base.metadata.create_all(engine)

    # create a session maker
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # query to retrieve all state objects and related city objs
    states_query = session.query(State).order_by(State.id).all()

    # display results
    for state in states_query:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_city_and_state(username, password, database)
