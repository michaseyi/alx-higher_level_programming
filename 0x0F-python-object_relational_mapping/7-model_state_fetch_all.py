#!/usr/bin/python3
"""This module contains the class definition of a State and
an instance of Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(engine)
    session = Session()

    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
