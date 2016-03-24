from unittest import main, TestCase
from flask import Flask, json
# import app

from sqlalchemy.orm import Session

# import serve
# import Models

from flask.ext.sqlalchemy import SQLAlchemy
# from models import Place, Type, Review, Photo, db
# from server import app
# from urllib.request import urlopen
# from solr import keyword_search

import warnings

class FunctionalTestCase(TestCase):

	# ----------
    # API Routes
    # ----------

    # --------------
    # Website Routes
    # --------------

	# Home Page
  #   def test_index_1(self):
		# r = self.app.get('/')
		# self.assertEqual(r.status, '200 OK')
    
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
    def test_about_1(self):
		r = self.app.get('/about')
		self.assertEqual(r.status, '200 OK')

    # Cities Page
    def test_cities(self):
		r = self.app.get('/cities')
		self.assertEqual(r.status, '200 OK')

	def test_cities_table(self):

	# Attractions Page
    def test_attractions_1(self):
		r = self.app.get('/attractions')
		self.assertEqual(r.status, '200 OK')

	def test_attractions_table(self):

	# Restaurants Page
    def test_restaurants_1(self):
		r = self.app.get('/restaurants')
		self.assertEqual(r.status, '200 OK')


    # def test_about_2 (self) :
    #     r = app.app.test_client().get('/about.html')
    #     c = r.headers['content-type']
    #     t = r.data.decode("utf-8")
    #     self.assertEqual(c, 'text/html; charset=utf-8')
    #     self.assertTrue('Derek Truong' in t)
    #     self.assertTrue('Jonathan Chu' in t)

