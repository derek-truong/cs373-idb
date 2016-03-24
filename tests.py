# from unittest import main, TestCase
# from flask import Flask, json
# # import app

# from sqlalchemy.orm import Session

# # import serve
# import models

# from flask.ext.sqlalchemy import SQLAlchemy
# # from models import Place, Type, Review, Photo, db
# # from server import app
# # from urllib.request import urlopen
# # from solr import keyword_search

from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from flask import *
from flask import request
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean

import threading
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash

from models import *

class FunctionalTestCase(TestCase):

    def test_write_city(self):
        query = session.query(city).all()
        startSize = len(query)

        session.add(city(name = "Austin", country="USA"))
        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize) 

    # s.query(Cities).filter(City.name == 'Barcelona').one()

    def test_write_city2(self):
        query = session.query(city).all()
        startSize = len(query)

        session.add(city(name = "Dallas", country="USA"))
        session.add(city(name = "Seattle", country="USA"))
        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 2, endSize)

    def test_write_city2(self):
        query = session.query(city).all()
        startSize = len(query)

        session.add(city(name = "Las Vegas", country="USA"))
        session.add(city(name = "Florida City", country="USA"))
        session.add(city(name = "New York City", country="USA"))
        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 3, endSize)

    def test_write_attraction(self):
        query = session.query(attractions).all()
        startSize = len(query)

        session.add(attractions(name = "Six Flags", Location="San Antonio"))
        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)

    def test_write_attraction2(self):
        query = session.query(attractions).all()
        startSize = len(query)

        session.add(attractions(name = "Sea World", Location="San Antonio"))
        session.add(attractions(name = "Miller Outdoor Theater", Location="Houston"))

        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 2, endSize)

    def test_write_attraction3(self):
        query = session.query(attractions).all()
        startSize = len(query)

        session.add(attractions(name = "University of Texas", Location="Austin"))
        session.add(attractions(name = "River Walk", Location="San Antonio"))
        session.add(attractions(name = "Statue of Liberty", Location="New York City"))

        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 3, endSize)

    def test_write_restaurant(self):
        query = session.query(attractions).all()
        startSize = len(query)

        session.add(restaurants(name = "Goode Company Seafood", Location="Houston"))

        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)

    def test_write_restaurant2(self):
        query = session.query(attractions).all()
        startSize = len(query)

        session.add(restaurants(name = "Cheesecake Factory", Location="Austin"))
        session.add(restaurants(name = "Gueros Taco Bar", Location="Austin"))

        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 2, endSize)

    def test_write_restaurant3(self):
        query = session.query(attractions).all()
        startSize = len(query)

        session.add(restaurants(name = "Don", Location="Austin"))
        session.add(restaurants(name = "Torchy's Tacos", Location="Austin"))
        session.add(restaurants(name = "Le Turtle", Location="New York City"))

        session.commit()
        query = session.query(city).all()

        endSize = len(query)

        self.assertEqual(startSize + 3, endSize)

	# ----------
    # API Routes
    # ----------
    def test_google_api(self):
        query = 'museums in austin, tx'
        self.assertEqual(r.)
    # --------------
    # Website Routes
    # --------------

	# Home Page
    def test_index_1(self):
		r = self.app.get('/')
		self.assertEqual(r.status, '200 OK')
    
    # def test_index_2(self):
    # 	r = app.app.test_client().get('')
    # 	c = r.headers['content-type']
    # 	t = r.data.decode("utf-8")
    # 	self.assertEqual(c, 'text/html; charset=utf-8')
    # 	self.assertTrue('Redirecting' in t)
    	
    # def test_html_index_3 (self) :
    #	r = app.app.test_client().get('/')
    #	c = r.headers['content-type']
    #	t = r.data.decode("utf-8")
    #	self.assertEqual(c, 'text/html; charset=utf-8')
    #	self.assertTrue('Cities' in t)
    #	self.assertTrue('Attractions' in t)
    #	self.assertTrue('Restaurants' in t)

    # About Page
 #    def test_about_1(self):
	# 	r = self.app.get('/about')
	# 	self.assertEqual(r.status, '200 OK')

 #    # Cities Page
 #    def test_cities(self):
	# 	r = self.app.get('/cities')
	# 	self.assertEqual(r.status, '200 OK')

	# def test_cities_table(self):

	# # Attractions Page
 #    def test_attractions_1(self):
	# 	r = self.app.get('/attractions')
	# 	self.assertEqual(r.status, '200 OK')

	# def test_attractions_table(self):

	# # Restaurants Page
 #    def test_restaurants_1(self):
	# 	r = self.app.get('/restaurants')
	# 	self.assertEqual(r.status, '200 OK')


    # def test_about_2 (self) :
    #     r = app.app.test_client().get('/about.html')
    #     c = r.headers['content-type']
    #     t = r.data.decode("utf-8")
    #     self.assertEqual(c, 'text/html; charset=utf-8')
    #     self.assertTrue('Derek Truong' in t)
    #     self.assertTrue('Jonathan Chu' in t)

