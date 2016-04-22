from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import *
from flask import request
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean
from sqlalchemy.ext.declarative import declarative_base
import threading
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
import app
from models import City, Restaurant, Attraction, Base

engine = create_engine('mysql+pymysql://travis:@localhost/test?charset=utf8')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
test_session = DBSession()

class FunctionalTestCase(TestCase):



    def test_city1(self):
        row = City(
            id=1,
            name='name',
            population=123456,
            country='country',
            demonym='demonym',
            elevation=1.0,
            description='description',
            image='image_url'
        )

        self.assertEqual(row.id ,1)
        self.assertEqual(row.name,'name')
        self.assertEqual(row.population,123456)
        self.assertEqual(row.country ,'country')
        self.assertEqual(row.demonym ,'demonym')
        self.assertEqual(row.elevation , 1.0)
        self.assertEqual(row.description , 'description')
        self.assertEqual(row.image,'image_url')

    def test_city2(self):
        row = City(
            id=2,
            name='fred',
            population=123456,
            country='country',
            demonym='demonym',
            elevation=1.0,
            description='description',
            image='image_url'
        )

        self.assertEqual(row.id ,2)
        self.assertEqual(row.name,'fred')
        self.assertEqual(row.population,123456)
        self.assertEqual(row.country ,'country')
        self.assertEqual(row.demonym ,'demonym')
        self.assertEqual(row.elevation , 1.0)
        self.assertEqual(row.description , 'description')
        self.assertEqual(row.image,'image_url')

    def test_city3(self):
        row = City(
            id=3,
            name='fred2',
            population=123456,
            country='country',
            demonym='dem0nym',
            elevation=1.0,
            description='description2',
            image='image_url'
        )

        self.assertEqual(row.id ,3)
        self.assertEqual(row.name,'fred2')
        self.assertEqual(row.population,123456)
        self.assertEqual(row.country ,'country')
        self.assertEqual(row.demonym ,'dem0nym')
        self.assertEqual(row.elevation , 1.0)
        self.assertEqual(row.description , 'description2')
        self.assertEqual(row.image,'image_url')


    def test_attraction1(self):
        row = Attraction(
            id=1,
            name='name',
            rating=12346,
            city_id=1,
            num_reviews=32,
            category='hi',
            image='image_url'
        )

        self.assertEqual(row.id ,1)
        self.assertEqual(row.name,'name')
        self.assertEqual(row.rating,12346)
        self.assertEqual(row.city_id ,1)
        self.assertEqual(row.num_reviews,32)
        self.assertEqual(row.category, 'hi')
        self.assertEqual(row.image,'image_url')

    def test_attraction2(self):
        row = Attraction(
            id=2,
            name='n4me',
            rating=12346,
            city_id=11,
            num_reviews=322,
            category='hi2',
            image='image_url'
        )

        self.assertEqual(row.id ,2)
        self.assertEqual(row.name,'n4me')
        self.assertEqual(row.rating,12346)
        self.assertEqual(row.city_id ,11)
        self.assertEqual(row.num_reviews,322)
        self.assertEqual(row.category, 'hi2')
        self.assertEqual(row.image,'image_url')

    def test_attraction3(self):
        row = Attraction(
            id=7,
            name='nam3',
            rating=1234226,
            city_id=1414,
            num_reviews=3222,
            category='h1',
            image='image_url'
        )

        self.assertEqual(row.id ,7)
        self.assertEqual(row.name,'nam3')
        self.assertEqual(row.rating,1234226)
        self.assertEqual(row.city_id ,1414)
        self.assertEqual(row.num_reviews,3222)
        self.assertEqual(row.category, 'h1')
        self.assertEqual(row.image,'image_url')

    def test_restaurant1(self):
        row = Restaurant(
            id=1,
            name='name',
            rating=12346,
            city_id=1,
            category='hi',
            address='1',
            image='image_url'
        )

        self.assertEqual(row.id ,1)
        self.assertEqual(row.name,'name')
        self.assertEqual(row.rating,12346)
        self.assertEqual(row.city_id ,1)
        self.assertEqual(row.category, 'hi')
        self.assertEqual(row.address, '1')
        self.assertEqual(row.image,'image_url')

    def test_restaurant2(self):
        row = Restaurant(
            id=11,
            name='name1',
            rating=123461,
            city_id=11,
            category='hi1',
            address='11',
            image='image_url1'
        )

        self.assertEqual(row.id ,11)
        self.assertEqual(row.name,'name1')
        self.assertEqual(row.rating,123461)
        self.assertEqual(row.city_id ,11)
        self.assertEqual(row.category, 'hi1')
        self.assertEqual(row.address, '11')
        self.assertEqual(row.image,'image_url1')

    def test_restaurant3(self):
        row = Restaurant(
            id=131,
            name='name31',
            rating=1234631,
            city_id=131,
            category='hi31',
            address='131',
            image='image_url31'
        )

        self.assertEqual(row.id ,131)
        self.assertEqual(row.name,'name31')
        self.assertEqual(row.rating,1234631)
        self.assertEqual(row.city_id ,131)
        self.assertEqual(row.category, 'hi31')
        self.assertEqual(row.address, '131')
        self.assertEqual(row.image,'image_url31')



    def test_serialize1(self):
        city = City(
            id=3,
            name='fred2',
            population=123456,
            country='country',
            demonym='dem0nym',
            elevation=1.0,
            description='description2',
            image='image_url'
        )
        city_dict = app.serialize(city)

        self.assertEqual(city_dict['name'], "fred2")

    def test_serialize2(self):
        restaurant = Restaurant(
            id=1,
            name='name',
            rating=12346,
            city_id=1,
            category='hi',
            address='1',
            image='image_url'
        )
        restaurant_dict = app.serialize(restaurant)

        self.assertEqual(restaurant_dict['name'], "name")

    def test_serialize3(self):
        attraction = Attraction(
            id=7,
            name='nam3',
            rating=1234226,
            city_id=1414,
            num_reviews=3222,
            category='h1',
            image='image_url'
        )
        attraction_dict = app.serialize(attraction)

        self.assertEqual(attraction_dict['name'], "nam3")


    def test_reload_data1(self):
        test_session.query(City).delete()
        app.reload_data(test_session, City,"Cities.json")
        city = test_session.query(City).filter_by(id=1).one()
        self.assertEqual(city.name, "Amsterdam")
        test_session.query(City).delete()

    def test_reload_data2(self):
        test_session.query(Restaurant).delete()
        app.reload_data(test_session, Restaurant, "Restaurants.json")
        restaurant = test_session.query(Restaurant).filter_by(id=5).one()
        self.assertEqual(restaurant.name, "Moonshine")
        test_session.query(Restaurant).delete()

    def test_reload_data3(self):
        test_session.query(Attraction).delete()
        app.reload_data(test_session, Attraction, "Attractions.json")
        attraction = test_session.query(Attraction).filter_by(id=5).one()
        self.assertEqual(attraction.name, "House of Torment")
        test_session.query(Attraction).delete()


if __name__ == "__main__" :
    main()

