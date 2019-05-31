# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:35:40 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
"""

import pandas as pd
import numpy as np

bca = pd.read_csv('material/Baltimore_City_Employee_Salaries_FY2014.csv')

bca.info()

# remove the dollar signs in the AnnualSalary field and assign it as a float

bca['AnnualSalary'] = bca['AnnualSalary'].astype(str)
bca['AnnualSalary'] = bca['AnnualSalary'].apply(lambda x: x.replace("$", ''))
bca['AnnualSalary'] = bca['AnnualSalary'].astype(float)

# Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
# Sort the data and display to show who get the highest salary

grouped_data = bca.groupby(by = ['JobTitle'])['AnnualSalary']
aggr = grouped_data.agg([sum, np.mean, max,min])
sorted_Salary = bca.sort_values(['AnnualSalary'],ascending=0)
print (str(sorted_Salary.iloc[0,0])+" got the highest salary")

#grouped_data.sort_values(by = 'mean', ascending = False).iloc[0,(0,2)]

# Try to group on JobTitle only and sort the data and display

grouped_job = bca.groupby(by = ['JobTitle']).agg(sorted)

# How many employess are there for each JobRoles and Graph it

uniq_emp = bca['JobTitle'].value_counts()[0:11].plot.bar()


# Graph and show which Job Title spends the most

spend = aggr.sort_values(by = ['sum'], ascending = 0)
spend['sum'][0:11].plot.bar()

print(spend.index[0]+ " spends the most")

# List All the Agency ID and Agency Name 

uniq_AgID = bca['AgencyID'].unique()
uniq_Ag = bca['Agency'].unique()

# Find all the missing Gross data in the dataset

missing_gross = bca.iloc[0:][bca['GrossPay'] == bca['GrossPay'].isnull()]
