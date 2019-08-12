#!/usr/bin/python3
'''Python script to list all City objects from database hbtn_0e_14_usa'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
