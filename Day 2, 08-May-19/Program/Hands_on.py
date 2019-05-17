# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:54:44 2019

@author: HIMANSHU SINGH
"""

"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

list1 = list(range(1,21))
list1

list1[::2] #for odd

list1[1::2] #for even

"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False 

def leapyear(year):
    if year%4 == 0 or (year%100 and year%400):
        print ("True")
    else:
        print ("False")
leapyear(2012)
        
        

"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year

print ("Enter any month like --> 'jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec'")

days_31 = ["jan","mar","may","jul","aug","oct","dec"]
days_30 = ["apr","jun","sep","nov"]

def days_in_month(str1):
    if str1 in days_31:
        print ("This month is of 31 days")
    elif str1 in days_30:
        print ("This month is of 30 days") 
    else:
        print ("This month is of 29 days")
    
days_in_month("jan")
    
    
    
