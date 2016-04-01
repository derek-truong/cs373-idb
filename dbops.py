
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, City, Attraction, Restaurant

engine = create_engine('sqlite:///swespt.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

"""
Adds any model object to the database
"""
def db_create(obj):
	session.add(obj)
	session.commit()

"""
Reads a specific object from the database of a specific type and id
"""
def db_read(type, id):
	return session.query(type).filter_by(id=id).one()
"""
Reads a specific object from the database of a specific type and id
"""
def db_read_all(type):
	return session.query(type).all()

