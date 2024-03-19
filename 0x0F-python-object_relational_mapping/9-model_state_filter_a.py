#!/usr/bin/python3
'''A script that lists all State objects from a database filtered by a
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_state_with_a(username, password, database):
    '''lists all state objs in a database filtered by a

    Args:
        username (str): username of database user
        password (str): password of database user
        database_name (str): name of database
    '''
    # define MySQl connection link(url)
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

    # query to retrieve all State objs sorted by id, in ascending order
    states = (
        session.query(State).order_by(State.id)
        .filter(State.name.like('%a%'))
    )

    # display results
    for state in states:
        print(f'{state.id}: {state.name}')

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_state_with_a(username, password, database)
