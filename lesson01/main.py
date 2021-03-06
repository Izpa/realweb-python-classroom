#!/usr/bin/python3

"""
    get_allcategories.py

    MediaWiki Action API Code Samples
    Demo of Allcategories module: GET request to list all categories
    on the English Wikipedia, starting from "15th-century caliphs".
    MIT license
"""

import requests


wikipedia_url = "http://en.wikipedia.org/w/api.php"
# http://en.wikipedia.org/w/api.php?
# action=query&list=allcategories&acprop=size&acprefix=hollywood&format=json"

wikipedia_params = {"action": "query",
                    "list": "allcategories",
                    "acprop": "size",
                    "acprefix": "hollywood",
                    "format": "json"}

res = requests.get(url=wikipedia_url, params=wikipedia_params)

data = res.json()

all_categories = data.get("query", {}).get("allcategories")

min_category_pages = None
min_category_name = ""

for category in all_categories:
    category_pages = int(category.get("pages"))
    category_name = category.get("*")

    if min_category_pages is None or category_pages < min_category_pages:
        min_category_pages = category_pages
        min_category_name = category_name

print(min_category_name, ":", min_category_pages)
