#!/usr/bin/python3
'''A script that updates the State object with id=2
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def update_state(username, password, database):
    '''updates the State obj with id=2 to 'New Mexico'

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

    # query id and update based on queried id
    state = (
        session.query(State).filter(State.id == 2)
    )
    state.update({State.name: 'New Mexico'})

    # commit the session to save the changes to database
    session.commit()

    # close the session
    session.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    update_state(username, password, database)
