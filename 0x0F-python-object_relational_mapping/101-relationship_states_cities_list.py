#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                     argv[1], argv[2], argv[3], pool_pre_ping=True))

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
