#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    pw = sys.argv[2]
    dbase = sys.argv[3]
    name = sys.argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, pw, dbase), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    state = session.query(State)
    .filter(State.name == name).order_by('id').first()
    print("{}".format(state.id))
