import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

"""
Model for cities.
It has a one to many relationship with both Attractions and Restaurants.
"""
class City(Base):

    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    elev = Column(Integer, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    desc = Column(String(255), nullable=False)   

"""
Model for attractions.
It has a many to one relationship with City
"""

class Attraction(Base):
    __tablename__ = 'attraction'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    rating = Column(Float, nullable=False)
    num_rating = Column(Integer, nullable=False)
    categ = Column(String(80), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    desc = Column(String(255), nullable=False)



"""
Model for restaurant.
It has a many to one relationship with City
"""
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    rating = Column(Float, nullable=False)
    categ = Column(String(30), nullable=False)
    address = Column(String(255), nullable=False) 


# engine = create_engine('mysql+mysqldb://swespt:@localhost/swespt?charset=utf8')
engine = create_engine('sqlite:///swespt.db')

Base.metadata.create_all(engine)