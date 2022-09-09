#!/usr/bin/python3
"""This module creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""
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
    new_state = State(name='California')
    new_state.cities.append(City(name='San Francisco'))
    session.add(new_state)
    session.commit()
