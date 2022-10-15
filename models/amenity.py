#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """defines the amenity class"""
    __tablename__
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
