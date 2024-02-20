#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a basic mysequel database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): new table name (users)
        email: (sqlalchemy String): an email of type string
        password (sqlalchemy String):  a password of type string
        first_name (sqlalchemy String): a user first_name as string
        last_name (sqlalchemy String): a last_name of type string
        places (sqlalchemy relationship): 
        reviews (sqlalchemy relationship)
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
