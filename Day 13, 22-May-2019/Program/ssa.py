# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:17:38 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
import pandas as pd
from zipfile import ZipFile
import numpy as np

df = pd.DataFrame(columns = ['Name','Sex','Number', 'Year'])
with ZipFile('material/baby_names.zip') as myzip:
    for i in range(1880, 2018):
        with myzip.open('yob'+str(i)+'.txt') as myfile:
            temp = pd.read_csv(myfile, names = ['Name','Sex','Number'])
            temp['Year'] = i
            df = pd.concat([df,temp])
            
# Display the top 5 male names of 2010
print(df[(df['Year'] == 2010) & (df['Sex'] == 'M')].sort_values(by =['Number'], ascending = False).head(5))

# Display the top 5 female names of 2010
print(df[(df['Year'] == 2010) & (df['Sex'] == 'F')].sort_values(by =['Number'], ascending = False).head(5))

# Calculate sum of the births column by sex as the total number of births 
# in that year(use pandas pivot_table method)
pivot_table = pd.pivot_table(df, values = 'Number' ,index = ['Year'], columns = ['Sex'], aggfunc = np.sum)
print(pivot_table)

# Plot the results of the above activity to show total births by sex and year
pivot_table.plot()
