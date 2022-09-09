#!/usr/bin/python3
"""This module ists all City objects from the database
hbtn_0e_101_usa"""
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
    for city in session.query(City):
        print("{}: {} -> {}".format(city.id, city.name,  city.state.name))
