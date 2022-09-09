#!/usr/bin/python3
"""This module contains the class definition of a State and
an instance of Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Represents the states table. Define objects that map to
    rows in the states table
    """

    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
