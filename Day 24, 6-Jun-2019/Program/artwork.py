# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:01:14 2019

@author: HIMANSHU SINGH
"""
"""
Q3.Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"1"
dataset = pd.read_csv('data.csv')
dataset.isnull().any(axis=0)
dataset.dropna(subset=["Country"] , axis=0, inplace=True)
him = dataset["Country"].value_counts()
name = him.index.tolist()
count = him.values.tolist()

plt.pie(count, labels=name, startangle=90, autopct='%2.2f%%', shadow=True)
plt.show()

---------------------------------------------------------------------------------
"2"
dataset = pd.read_csv('data.csv')
dataset.isnull().any(axis=0)
dataset.dropna(subset=["Classification"] , axis=0, inplace=True)
him = dataset["Classification"].value_counts().head(2)
name = him.index.tolist()
count = him.values.tolist()

import numpy as np
import matplotlib.pyplot as plt

y_pos = np.arange(len(name))

plt.bar(y_pos, count, align='center', alpha=0.6)
plt.xticks(y_pos, name)
plt.ylabel('Number')
plt.title('top 2 classification for the artworks')

plt.show()
---------------------------------------------------------------------------------
"4"
dataset = pd.read_csv('data.csv')
dataset.isnull().any(axis=0)
dataset.dropna(subset=["Culture"] , axis=0, inplace=True)
him = dataset["Culture"].value_counts().head(2)
name = him.index.tolist()
count = him.values.tolist()

y_pos = np.arange(len(name))

plt.bar(y_pos, count, align='center', alpha=0.6)
plt.xticks(y_pos, name)
plt.ylabel('Number')
plt.title('top 2 culture for the artworks')

plt.show()