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

    name = argv[4]

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    for state in session.query(State).filter(State.name == name).all():
        if state.name == argv[4]:
            print(state.id)
            session.close()
            exit()
    print("Not found")
    session.close()
