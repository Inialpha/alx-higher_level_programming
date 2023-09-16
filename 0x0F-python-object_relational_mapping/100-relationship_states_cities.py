#!/usr/bin/python3
"""A script that creates the State “California” with the City “San Francisco"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import State, Base
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                     argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    new_city = City(name="San Francisco", state=State(name="California"))
    session.add(new_city)
    session.commit()
