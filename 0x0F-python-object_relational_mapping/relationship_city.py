#!/usr/bin/python3
"""This module contains the City class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class City(Base):
    """This class defines a city object"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
