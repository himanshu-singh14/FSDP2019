# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:56:48 2019

@author: HIMANSHU SINGH
"""

# Weighted Score Calculator

print ("Enter all number 3 for assignment and then 2 for exams")
a1 = int(input("Enter First number :"))
a2 = int(input("Enter Second number :"))
a3 = int(input("Enter Third number :"))
e1 = int(input("Enter Fourth number :"))
e2 = int(input("Enter Fifth number :"))

weighted_score = (a1 + a2 + a3)*0.1 + (e1 + e2)*0.35

sws = str(weighted_score)
print("Weighted Score : "+sws)