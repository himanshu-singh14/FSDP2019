# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:41:15 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""

user_input = input("Enter file name with txt extention in double quoted comma :")
with open(user_input, 'rt') as file :
    print(file.

import csv

with open("romeo.") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")    
    for row in csv_reader:
        print (row)


