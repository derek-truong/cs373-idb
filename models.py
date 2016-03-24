import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class City(Base):

    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    desc = Column(String(255), nullable=False)   

class Attraction(Base):
    __tablename__ = 'attraction'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    desc = Column(String(255), nullable=False)   

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    categ = Column(String(30), nullable=False)
    address = Column(String(255), nullable=False) 


engine = create_engine('mysql+mysqldb://swespt:@localhost/swespt?charset=utf8')
Base.metadata.create_all(engine)