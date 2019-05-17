# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:50:02 2019

@author: HIMANSHU SINGH
"""

# Replacing of Charactors

str1 = "RESTART"
str1.replace('R', '$')

str1[0]+str1[1:].replace('R','$')

index = str1.find('R')

str1[:index+1]+str1[index+1:].replace('R','$')

