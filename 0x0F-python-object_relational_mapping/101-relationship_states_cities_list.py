#!/usr/bin/python3
"""This module lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    count = [1, 1]
    for state in session.query(State):
        print("{}: {}".format(count[0], state.name))
        for city in state.cities:
            print("    {}: {}".format(count[1], city.name))
            count[1] += 1
        count[0] += 1
