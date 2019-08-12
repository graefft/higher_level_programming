#!/usr/bin/python3
'''Python script to list State objects from hbtn_0e_6_usa with letter a'''


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

    a_states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    for state in a_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
