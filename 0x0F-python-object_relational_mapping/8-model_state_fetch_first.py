#!/usr/bin/python3
"""This module contains the class definition of a State and
an instance of Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
import sys

Base = declarative_base()


class State(Base):
    """Represents the states table. Define objects that map to
    rows in the states table
    """

    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
