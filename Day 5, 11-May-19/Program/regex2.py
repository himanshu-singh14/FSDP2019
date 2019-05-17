# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:44:18 2019

@author: HIMANSHU SINGH
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

import re
ls = []
while True:
    N = input("Enter email : ")
    if N == "":
        break
    if re.findall(r'^[a-z0-9_\.-]+@[0-9a-z]+\.[a-z]{2,4}$', N):
        ls.append(re.findall(r'^[a-z0-9_\.-]+@[0-9a-z]+\.[a-z]{2,4}$', N))
print(sorted(ls))    







