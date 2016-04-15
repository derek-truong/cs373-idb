import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy_fulltext import FullText, FullTextSearch

Base = declarative_base()

"""
Model for cities.
It has a one to many relationship with both Attractions and Restaurants.
"""
class City(Base):

    __tablename__ = 'city'

    # __table_args__ = {'mysql_engine':'MyISAM',
    #                   'mysql_charset':'utf8'}

    #__fulltext_columns__ = ('id','name','population','country','demonym','elevation','description','image')

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    population = Column(Integer, nullable=False)
    country = Column(String(80), nullable=False)
    demonym = Column(String(80), nullable=False)
    elevation = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)     

    # def __init__(self, id, name,population,country,demonym,elevation,description,image) :
    #     self.id = id
    #     self.name = name
    #     self.population = population
    #     self.country = country
    #     self.demonym = demonym
    #     self.elevation = elevation
    #     self.description = description
    #     self.image = image
"""
Model for attractions.
It has a many to one relationship with City
"""

class Attraction(Base):
    __tablename__ = 'attraction'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    rating = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    num_reviews = Column(Integer, nullable=False)
    category = Column(String(80), nullable=False)
    image = Column(String(255), nullable=False) 


"""
Model for restaurant.
It has a many to one relationship with City
"""
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    rating = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    category = Column(String(30), nullable=False)
    address = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)  


engine = create_engine('sqlite:///swespt.db')
# if __name__ == '__main__':
# engine = create_engine('mysql+pymysql://guestbook-admin:my-guestbook-admin-password@pythonwebapp_db/guestbook')
# engine = create_engine('mysql://admin:password@localhost/swespt')
Base.metadata.create_all(engine)