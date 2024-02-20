#!/usr/bin/python3
"""Describes a new city class"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a new city for mysequel database.

    Grandchild of SQLAlchemy Base and links to the mysequel table.

    Attributes:
        __tablename__ (str): The name of the mysequel table for storing Cities.
        name (sqlalchemy String): The name of the single City.
        state_id (sqlalchemy String): The state id of the single City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
