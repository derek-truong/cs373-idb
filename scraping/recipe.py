#!/usr/bin/env python3
import requests
import json

recipes = []

# get recipes from page 1 to 39
for i in range(1, 40):
	response = requests.get("http://swedishchef.me/recipes?page=" + str(i))
	data = response.json()

	# print the recipes for a given page
	for item in data["recipes"]:
		recipe = {"cuisine": item["cuisine"], "id": item["id"], 
            "image_uri": item["image_uri"], 
            "ready_in_minutes": item["ready_in_minutes"],
            "servings": item["servings"], "title": item["title"]
            }
		recipes.append(recipe)

with open('recipes.json', 'w') as outfile:
	json.dump(recipes, outfile)