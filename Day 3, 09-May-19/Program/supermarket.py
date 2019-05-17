# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:06:20 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

dic = {}
while True:
    user_input = input()
    ls = user_input.split(" ")
    values = ls.pop()
    if user_input != "":
        if ' '.join(ls) in dic:
            dic[' '.join(ls)] += int(values)
        else:
            dic[' '.join(ls)] = int(values)
    if not user_input:
        break
print(dic)














