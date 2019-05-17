# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:48:40 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import json
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Allahabad"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)

response = requests.get(url)
response.text
jsondata = response.json()
print (jsondata.keys())
for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
   
print("Temprature : "+str(jsondata["main"]["temp"]))
print("Latitude : "+str(jsondata["coord"]["lat"])+"  Longitude : "+str(jsondata["coord"]["lon"]))
print("Weather Condition : "+jsondata["weather"][0]["main"])
print("Wind Speed : "+str(jsondata["wind"]["speed"]))
print("Sunrise : "+str(jsondata["sys"]["sunrise"])+"  Sunset : "+str(jsondata["sys"]["sunset"]))




