#!/usr/bin/python3
'''A script that deletes the State object with letter a
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def delete_states_with_a(username, password, database):
    '''deletes the State obj with letter a

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

    # query and retrieve all State objs with a in them
    states_to_del = (
        session.query(State).filter(State.name.like('%a%')).all()
    )

    # delete the queried state objs
    for state in states_to_del:
        session.delete(state)

    # commit the session to save the changes to database
    session.commit()

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    delete_states_with_a(username, password, database)
