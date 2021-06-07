from sqlalchemy.sql.expression import table
from . import Base
from sqlalchemy import Column, Integer, String



class User( Base ):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    passwd = Column(String, nullable=False)
    
    
    def __repr__( self ):
        return f"< User -> '{ self.id }' >"

