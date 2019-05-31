# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:51:23 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    To perfrom analysis on the Telecom industry churn dataset -
    1. Predict the count of Churned customer availing both voice mail plan and international plan schema
    2. Total charges for international calls made by churned and non-churned customer and visualize it
    3. Predict the state having highest night call minutes for churned customer
    4. Visualize -
        a. the most popular call type among churned user
        b. the minimum charges among all call type among churned user
    5. Which category of customer having maximum account lenght? Predict and print it
    6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
    7. In which area code the international plan is most availed?
"""


import pandas as pd

tel = pd.read_csv("material/Telecom_churn.csv")

# Predict the count of Churned customer availing both voice mail plan and international plan schema

churned_users = tel[tel['churn'] == True]         # churned users found out
non_churned_users = tel[tel['churn'] == False]    # non churned users found out

churn_int_voice = churned_users['churn'][(churned_users['voice mail plan'] == 'yes')
                         & (churned_users['international plan'] == 'yes')].count()

print("Count of Churned customer availing both voice mail plan and international plan: ",churn_int_voice)


# Total charges for international calls made by churned and non-churned customer and visualize it

tot_int_chrg_churn = churned_users['total intl charge'].sum()
tot_int_chrg_non_churn = non_churned_users['total intl charge'].sum()

print("Total charges for international calls made by churned users: ",tot_int_chrg_churn)
print("Total charges for international calls made by non-churned users: ",tot_int_chrg_non_churn)

tot_int_chrg = tel.groupby('churn')['total intl charge'].sum()
tot_int_chrg.plot.pie(autopct = '%2.2f%%')


# Predict the state having highest night call minutes for churned customer

max_state = churned_users[['state', 'total night minutes']][churned_users['total night minutes'] == churned_users['total night minutes'].max()]

print("State having highest night call minutes for churned customer: ",max_state)


# visualize the most popular call type among churned user

pop_calls = churned_users.iloc[:, 7:19].sum()
pop_calls.plot.bar()


# Which category of customer having maximum account lenght? Predict and print it

churned_acc_len = churned_users['account length'].max()
non_churned_acc_len = tel['account length'][tel['churn'] == False].max()


if churned_acc_len > non_churned_acc_len:
    print('churned user have the maximum account lenght')
else:
    print('regular user have the maximum account lenght')


# Predict a relation between the customer and customer care service that 
# whether churned customer have shown their concern to inform the customer care service about their problem or not

cus_care_ser = churned_users['customer service calls'].sum()

print("Total Cuutomer care calls by churned users: ",cus_care_ser)


# In which area code the international plan is most availed?

area_most_int = tel.groupby('area code')['international plan'].value_counts().unstack().sort_values(by = 'yes', ascending = False)

area_most_int.plot.bar()

print("Area code in which international plan is most availed:", area_most_int)