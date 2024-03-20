#!/usr/bin/python3
'''A script that creates the State California with the city San Francisco
from a database
'''
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def create_state_and_city(username, password, database):
    '''creates the State California with the city San Francisco
    from a database

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

    # create a new State object
    state_object = State(name='California')

    # create a new City object
    state_object.cities = [City(name='San Francisco')]

    # add state object to session
    session.add(state_object)

    # commit and save to database
    session.commit()

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    create_state_and_city(username, password, database)
