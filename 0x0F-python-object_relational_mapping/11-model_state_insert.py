#!/usr/bin/python3
'''Python script to insert Louisiana into hbtn_0e_6_usa with'''


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

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(session.query(State).filter_by(name="Louisiana").first().id)

    session.close()
