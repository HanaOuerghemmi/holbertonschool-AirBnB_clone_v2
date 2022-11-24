#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'review'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('places.id'), nullable=False)
