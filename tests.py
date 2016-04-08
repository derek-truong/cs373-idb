from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from flask import *
from flask import request
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean

import threading
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash

from models import *
from dbops import *

class FunctionalTestCase(TestCase):

    def test_db_create1(self):
        drop_table(City)
        query = session.query(City).all()
        startSize = len(query)

        temp_city = {"id": 55,"name": "Dallas","population": 5000, "country": "USA", "demonym": "American", "elevation": 100000.0, "description": "Dallas is Great", "image": "url"}
        
        db_create(City(**temp_city))
        query = session.query(City).all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize) 

    def test_db_create2(self):
        drop_table(Restaurant)
        query = session.query(Restaurant).all()
        startSize = len(query)

        restaurant = {"id": 200, "name": "Don", "rating": 5, "category": "Japanese",
               "address": "Guadalupe", "city_id": 55, "image": "url"
          }
        db_create(Restaurant(**restaurant))
        query = session.query(Restaurant).all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize) 

    def test_db_create3(self):
        drop_table(Attraction)
        query = session.query(Attraction).all()
        startSize = len(query)

        attraction = {"id": 200, "name": "Six Flags", "rating": 5, "category": "Amusement Park",
                 "num_reviews": 50, "city_id": 55, "image": "url"
            }
        db_create(Attraction(**attraction))
        query = session.query(Attraction).all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize) 

    def test_db_read1(self):
        temp_city = db_read(City, 55)
        self.assertEqual(temp_city.name, "Dallas")

    def test_db_read2(self):
        temp_restaurant = db_read(Restaurant, 200)
        self.assertEqual(temp_restaurant.name, "Don")

    def test_db_read3(self):
        temp_attraction = db_read(Attraction, 200)
        self.assertEqual(temp_attraction.name, "Six Flags")

    def test_db_read_all1(self):
        city_list = db_read_all(City)
        self.assertEqual(city_list[0].name, "Dallas")

    def test_db_read_all2(self):
        restaurant_list = db_read_all(Restaurant)
        self.assertEqual(restaurant_list[0].name, "Don")

    def test_db_read_all3(self):
        attraction_list = db_read_all(Attraction)
        self.assertEqual(attraction_list[0].name, "Six Flags")

    def test_serialize1(self):
        city = session.query(City).filter_by(id=1).one()
        city_dict = serialize(city)

        self.assertEqual(city_dict['name'], "Amsterdam")

    def test_serialize2(self):
        restaurant = session.query(Restaurant).filter_by(id=5).one()
        restaurant_dict = serialize(restaurant)

        self.assertEqual(restaurant_dict['name'], "Moonshine")

    def test_serialize3(self):
        attraction = session.query(Attraction).filter_by(id=5).one()
        attraction_dict = serialize(attraction)

        self.assertEqual(attraction_dict['name'], "House of Torment")

    def test_drop_table2(self):
        drop_table(Restaurant)
        query = session.query(Restaurant).all()
        endSize = len(query)

        self.assertTrue(endSize == 0)

    def test_drop_table3(self):
        drop_table(Attraction)
        query = session.query(Attraction).all()
        endSize = len(query)

        self.assertTrue(endSize == 0)

    def test_drop_table1(self):
        drop_table(Restaurant)
        drop_table(Attraction)
        drop_table(City)
        query = session.query(City).all()
        endSize = len(query)

        self.assertTrue(endSize == 0)

    def test_reload_data1(self):
        reload_data(City,"Cities.json")
        city = session.query(City).filter_by(id=1).one()
        self.assertEqual(city.name, "Amsterdam")

    def test_reload_data2(self):
        reload_data(Restaurant, "Restaurants.json")
        restaurant = session.query(Restaurant).filter_by(id=5).one()
        self.assertEqual(restaurant.name, "Moonshine")

    def test_reload_data3(self):
        reload_data(Attraction, "Attractions.json")
        attraction = session.query(Attraction).filter_by(id=5).one()
        self.assertEqual(attraction.name, "House of Torment")

    def test_db_city_join1(self):
        reload_data(City,"Cities.json")
        restaurant_list = db_city_join(Restaurant)
        self.assertEqual(restaurant_list[0][0].name, "Restaurant De Kas")
        self.assertEqual(restaurant_list[0][1].name, "Amsterdam")

    def test_db_city_join2(self):
        attraction_list = db_city_join(Attraction)
        self.assertEqual(attraction_list[0][0].name, "Anne Frank House")
        self.assertEqual(attraction_list[0][1].name, "Amsterdam")

    def test_db_city_join3(self):
        attraction_list = db_city_join(Attraction)
        self.assertEqual(attraction_list[4][0].name, "House of Torment")
        self.assertEqual(attraction_list[4][1].name, "Austin")

    def test_db_city_join4(self):
        restaurant_list = db_city_join(Restaurant)
        self.assertEqual(restaurant_list[20][0].name, "Neptune Oyster")
        self.assertEqual(restaurant_list[20][1].name, "Boston")

    def test_db_read_city_spots1(self):
        restaurant_list = db_read_city_spots(Restaurant, 55)
        self.assertEqual(restaurant_list[0].name, "Don")

    def test_db_read_city_spots2(self):
        attraction_list = db_read_city_spots(Attraction, 55)
        self.assertEqual(attraction_list[0].name, "Six Flags")


if __name__ == "__main__" :
    main()  

