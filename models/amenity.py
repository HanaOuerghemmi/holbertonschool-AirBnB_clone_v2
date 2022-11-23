#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey

class Amenity(BaseModel):
    __tablename__= 'amenities'
    name = Column(String(1024), nullable=False)
