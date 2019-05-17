# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:46:25 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import json
import requests
response = requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=2e3ca519e7a9df33cb00")
print(response.text)





