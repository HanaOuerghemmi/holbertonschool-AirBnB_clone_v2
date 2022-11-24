from sqlalchemy import Column, Integer, Sequence, String, DateTime
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """ initialize of anew bd create the engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ """
        objs = {}
        if cls:
            for o in self.__session.querry(cls).all():
                objs[o.__class__.__name__ +'.'+ o.id] = o
            return objs
        else:
            for o in self.__session.querry(User,
                                          State, City, Place,
                                          Amenity, Review).all():
                objs[o.__class__.__name__ +'.'+ o.id] = o
            return objs
                
    def new(self, obj):
        """ """
        self.__session.add(obj)
    
    def save(self):
        """ """
        self.__session.commit()
    def delete(self, obj=None):
        """ """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,expire_on_commit=False)
        Session = scoped_session(session_factory)
    
