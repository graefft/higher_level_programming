#!/usr/bin/python3
'''Script to change State with id 2 to New Mexcio'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    query = session.query(State).filter(State.id == 2).first()
    query.name = "New Mexico"

    session.commit()
    session.close()
