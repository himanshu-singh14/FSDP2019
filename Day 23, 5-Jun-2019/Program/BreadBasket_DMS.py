# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:58:23 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery
    retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.

"""
# Apriori

# Importing the libraries
import pandas as pd
from apyori import apriori
from itertools import chain 
import operator
import matplotlib.pyplot as plt

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')

keys2D = dataset.iloc[:, [3]].values.tolist()
keys = list(chain.from_iterable(keys2D))

set_key = list(set(keys))

set2_key = set()
new_dict = {}
for item in keys:
    if item not in set2_key:
        new_dict[item] = 1
    else:
        new_dict[item] += 1
    set2_key.add(item)

sorted_d = sorted(new_dict, key=new_dict.get, reverse=True)

pei_keys = []
pei_values = []
num = 0
for item in sorted_d :
    if(num < 15):
        pei_keys.append(item)
    num += 1    
num2  = 0   
for item in sorted_d :
    if(num2 < 15):
        pei_values.append(new_dict[item])
    num2 += 1

plt.pie(pei_values, labels=pei_keys, startangle=90, autopct='%.1f%%')
plt.show()

===============================================================================



transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)




for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")


