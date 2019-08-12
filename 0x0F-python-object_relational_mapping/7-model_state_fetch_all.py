#!/usr/bin/python3
'''Python script to list all State objects from database hbtn_0e_6_usa'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
    session.close()
