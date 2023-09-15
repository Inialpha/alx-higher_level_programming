#!/usr/bin/python3
"""A script that prints all cities in a state"""
from model_state import State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, pw, dbase), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    cities = session.query(State, City).filter(City.state_id
                                               == State.id).order_by(City.id)
    for state, city in cities:
        print("{} ({}) {}".format(state.name, city.id, city.name))
