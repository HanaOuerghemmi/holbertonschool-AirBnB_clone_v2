#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """return the list of city instance from file storage"""
            clist = []
            for city in list(models.storage.all(City).values()):
                if city.sate_id == self.id:
                    clist.append(city)
            return clist
