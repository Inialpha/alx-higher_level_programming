#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    pw = sys.argv[2]
    dbase = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, pw, dbase))

    #Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by('id').all()
    for state in states:
        print(state.id, state.name)
