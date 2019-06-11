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

"""
index = dataset.index[dataset["Item"]=="NONE"].tolist()
dataset.drop(index , axis=0, inplace=True)

him = dataset["Item"].value_counts().head(15)
name = him.index.tolist()
count = him.values.tolist()

plt.pie(count, labels=name, startangle=90, autopct='%2.2f%%', shadow=True)
plt.show()

"""

===========================================================================================

import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

index = dataset.index[dataset["Item"]=="NONE"].tolist()
dataset.drop(index , axis=0, inplace=True)

him = dataset["Item"].value_counts()

z = list(zip(name,count))
for item in z:
    print ("support of ",item[0]," is ",str(item[1]/20507))



item = dataset.groupby("Transaction")["Item"].unique()
item_list = [x.tolist() for x in item]


for pp in name:
    kk = 0
    for ll in item_list:
        if "Sandwich" in ll and pp in ll:
            kk += 1  
    print(str(kk/680)+" --> Confidence of Sandwich -> "+pp)

   
kkk = 0
for ll in item_list:
    if "Coke" in ll:
        kkk+=1
kkk/9465

(852*9465)/(4528*3097)
transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset

rules = apriori(item_list, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)


49/184

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
    


import pandas as pd

df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
df.head()
df.isnull().any(axis=0)

df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['Description','CustomerID'], inplace=True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

df.head()

 
basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

rules = apriori(basket_sets, min_support=0.07,min_confidence = 0.25, min_lift = 3)

results = list(rules)



