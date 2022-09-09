#!/usr/bin/python3
"""This module contains the class definition of a City"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """Represents the cities table. Define objects that map to
    rows in the cities table
    """

    __tablename__ = "cities"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('states.id', ondelete='CASCADE'))
