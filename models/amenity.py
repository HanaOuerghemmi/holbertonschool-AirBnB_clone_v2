#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(1024), nullable=False)
    """place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)"""
