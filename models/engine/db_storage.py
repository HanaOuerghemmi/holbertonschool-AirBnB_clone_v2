from sqlalchemy import Column, Integer, Sequence, String, DateTime
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel


Class DBStorage:
    """ DBStorage class"""

    __engine = None
    __session = None
   def __init__(self):
        """ initialize of anew bd create the engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}
                                    .format(getenv('HBNB_MYSQL_USER'), 
                                            getenv('HBNB_MYSQL_PWD'),
                                            getenv('HBNB_MYSQL_HOST'),
                                            getenv('HBNB_MYSQL_DB')), 
                                    pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
