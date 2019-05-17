# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:37:44 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

import csv

dic = {}
st = set()
value = 1
with open("romeo.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")    
    for row in csv_reader:
        for word in row:
            if word not in st:
                dic[''.join(word)] = value
            else:
                dic[''.join(word)] += value
            st.add(word)
print(dic)  