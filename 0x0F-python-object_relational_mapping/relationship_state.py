#!/usr/bin/python3
"""This module contains the State class"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship
from relationship_city import City, Base


class State(Base):
    """This class defines the State object"""
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
