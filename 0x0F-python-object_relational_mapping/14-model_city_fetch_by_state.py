#!/usr/bin/python3
"""This module displays all cities in the database"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(engine)
    session = Session()

    for city in session.query(City):
        print("{}: ({}) {}".format(
            city.state.name,
            city.id,
            city.name
        ))
