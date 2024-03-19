#!/usr/bin/python3
'''A script that prints State object with name passed as arg
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def print_state_name(username, password, database, name):
    '''prints the State obj with the name passed as arg
    from a database

    Args:
        username (str): username of database user
        password (str): password of database user
        database_name (str): name of database
        name (str): name of state to search
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
    state = (
        session.query(State).filter(State.name == name).first()
    )

    # display results
    if state:
        print(f'{state.id}')
    else:
        print('Not found')

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    print_state_name(username, password, database, name)
