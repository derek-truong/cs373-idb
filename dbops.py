
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, class_mapper
from models import Base, City, Attraction, Restaurant
import json
engine = create_engine('sqlite:///swespt.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class AlchemyEncoder(json.JSONEncoder):
    def default(self, o):
        print("BOI I DONT WORK")
        if isinstance(o, tuple):
            data = {}
            for obj in o:
                data.update(self.parse_sqlalchemy_object(obj))
            return data
        if isinstance(o.__class__, DeclarativeMeta):
            return self.parse_sqlalchemy_object(o)
        return json.JSONEncoder.default(self, o)

    def parse_sqlalchemy_object(self, o):
        data = {}
        fields = o.__json__() if hasattr(o, '__json__') else dir(o)
        for field in [f for f in fields if not f.startswith('_') and f not in ['metadata', 'query', 'query_class']]:
            value = o.__getattribute__(field)
            try:
                json.dumps(value)
                data[field] = value
            except TypeError:
                data[field] = None
        return data

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


"""
Drops a table of a certain type
"""
def drop_table(type):
	session.query(type).delete()

def db_city_join(type):
	return session.query(type, City).filter(type.city_id == City.id).all()

def serialize(model):
	# """Transforms a model into a dictionary which can be dumped to JSON."""
	columns = [c.key for c in class_mapper(model.__class__).columns]
	return dict((c, getattr(model, c)) for c in columns)

def reload_data(type, file_path):
	with open(file_path) as json_file:
		# print(json_file.read())
		json_data = json.load(json_file)
	for x in json_data:
		db_create(type(**x))
	# print(json_data)
# db_create(City(name="Cool City1", population = 500, country = "US", demonym="idk", elevation= 1, description = "coolest place in Texas"))
# db_create(Attraction(name="Attraction1", city_id=1, rating = 3, num_reviews=50, category="Landmark"))

# for x in db_read_all(Attraction):
# 	print(str(x.id) + "name: " + x.name)