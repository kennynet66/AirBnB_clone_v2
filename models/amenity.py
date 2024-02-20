#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents a new Amenity for mysequel DB.

    Attributes:
        __tablename__ (str): The table name
        name (sqlalchemy String): The new amenity name.
        place_amenities (sqlalchemy relationship): Relationship Place-Amenity.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
