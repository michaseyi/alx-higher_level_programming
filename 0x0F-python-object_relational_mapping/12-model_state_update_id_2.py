#!/usr/bin/python3
"""This module contains changes the name of a State
object from the database hbtn_0e_6_usa"""
from re import U
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
    state = session.query(State).where(State.id == 2).one_or_none()
    if state is not None:
        state.name = 'New Mexico'
    session.commit()
