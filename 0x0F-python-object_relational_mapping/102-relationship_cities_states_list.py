#!/usr/bin/python3

"""A script that lists all City objects from the database"""

from sys import argv
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                     argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
