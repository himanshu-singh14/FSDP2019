# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:44:13 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

import csv

with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")    
    for row in csv_reader:
        print (row)
 
""" --------------------------------------------------------- """
       
st = set()    
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",") 
    next(csv_reader)
    for row in csv_reader:
        st.add(row[0])
print(st)        

""" --------------------------------------------------------------"""
st = set()  
dic = {}
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",") 
    next(csv_reader)
    for row in csv_reader:
        if row[0] not in st:
            dic[''.join(row[0])] = int(row[2])
        else:
            dic[''.join(row[0])] += int(row[2])
        st.add(row[0])
print(st)  
print(dic)

""" --------------------------------------------------------------"""

total = 0    
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",") 
    next(csv_reader)
    for row in csv_reader:
        total = total + int(row[2])
print(total)





