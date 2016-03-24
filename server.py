"""Cloud Foundry test"""
from flask import Flask, render_template, request
import os
import requests
import json
import csv

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))


#Splash/Home page
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('index.html')

#Park detail page
@app.route('/parks/<int:park_id>')
def park_detail(park_id):
	return render_template('cities.html')

#Restaurant detail page
@app.route('/restaurants/<int:r_id>')
def restaurant_detail(r_id):
	return render_template('attractions.html')

# Parks Table
@app.route('/parks')
def parks():
	return render_template('cities.html')

# Restaurants Table
@app.route('/restaurants')
def restaurants():
	return render_template('attractions.html')

@app.route('/about')
def about():
	return render_template('about.html')







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
