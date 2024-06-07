from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base): #con esto le digo que va a ser una entidad de mi bd

    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
