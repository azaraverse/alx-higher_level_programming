#!/usr/bin/python3
'''Prints all city objects from a database
'''
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City
import sys


def fetch_cities(username, password, database):
    '''Prints all City objects from the database hbtn_0e_14_usa

    Args:
        username (str): username of database user
        password (str): password of database user
        database (str): name of database
    '''
    # initialise connection url
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

    # query to retreive all cities
    query_cities = (
        session.query(City, State)
        .join(State)
        .order_by(City.id)
        .all()
    )

    # display results
    for city, state in query_cities:
        print(f'{state.name}: ({city.id}) {city.name}')

    # close session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_cities(username, password, database)
