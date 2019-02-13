#!/usr/bin/python3

"""
    get_allcategories.py

    MediaWiki Action API Code Samples
    Demo of Allcategories module: GET request to list all categories
    on the English Wikipedia, starting from "15th-century caliphs".
    MIT license
"""
import json

import pandas
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

allcategories = data.get("query", {}).get("allcategories")

# Переименовываем поле "*"
for categories in allcategories:
    categories["name"] = categories.get("*")
    categories.pop("*")

# Конвертируем данные в json
allcategories_as_json = json.dumps(allcategories)

# Конвертируем json d специальный формат пандаса - датафрейм
pandas_dataframe = pandas.read_json(allcategories_as_json)

# Cохраняем датафрейм как ексель
pandas_dataframe.to_excel("example.xlsx")

