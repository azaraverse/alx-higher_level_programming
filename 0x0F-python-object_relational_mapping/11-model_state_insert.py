#!/usr/bin/python3
'''A script that adds the State object 'Louisiana'
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def add_state(username, password, database):
    '''adds the State obj 'Louisiana' to the database

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

    # create a new State obj
    state = State(name='Louisiana')

    # add the new State obj to the session
    session.add(state)

    # commit the session to save the changes to database
    session.commit()

    # display results (using state's id)
    print(state.id)

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    add_state(username, password, database)
