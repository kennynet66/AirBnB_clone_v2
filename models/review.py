#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a single review for a mysequel database.

    Inherits from SQLAlchemy Base and links to the MySQL table reviews.

    Attributes:
        __tablename__ (str):Where to store the reviews
        text (sqlalchemy String): review to be stored
        place_id (sqlalchemy String): The reviews place id
        user_id (sqlalchemy String): the id of the user who made the review
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
