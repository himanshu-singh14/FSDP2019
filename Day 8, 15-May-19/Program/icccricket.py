# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:33:30 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

from bs4 import BeautifulSoup
import requests
# import urllib

#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table', class_='table')
# print (right_table.prettify())

#Generate lists
A=[]
B=[]

tbdy = right_table.tbody
# print(tbdy)
# print( tbdy.tr.findAll('td')[1].text.strip()) // print england only
for row in tbdy.findAll('tr'):
    cells = row.findAll('td')
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["Rank","Team"]
col_data = OrderedDict(zip(col_name,[A,B]))
df = pd.DataFrame(col_data) 
df.to_csv("odi_rank.csv")
