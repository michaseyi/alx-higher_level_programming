#!/usr/bin/python3
"""This module contains the class definition of a State table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from relationship_city import Base, City


class State(Base):
    """Represents the states table. Define objects that map to
    rows in the states table
    """

    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship(
        'City', cascade='all, delete',  back_populates='state')


City.state = relationship('State', back_populates='cities')
