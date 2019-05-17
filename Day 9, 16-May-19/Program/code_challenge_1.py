# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:03:06 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Database handling using sqlite 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os
import sqlite3
from pandas import DataFrame
#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')
# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_University.db' )
# creating cursor
c = conn.cursor()
# STEP 1
# www.sqlite.org/datatype3.html
# c.execute ("DROP TABLE Students")
c.execute ("""CREATE TABLE Students(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTIGER,
          Student_Branch TEXT
          )""")
# STEP 2
c.execute("INSERT INTO Students VALUES ('Sylvester', 50, 1 , 'CSE')")
c.execute("INSERT INTO Students VALUES ('Yogendra', 40, 2 , 'IT')")
c.execute("INSERT INTO Students VALUES ('Pradeep', 30, 3 , 'ECE')")
c.execute("INSERT INTO Students VALUES ('Kunal', 30, 4 , 'ME')")
c.execute("INSERT INTO Students VALUES ('Devendra', 49, 5 , 'IT')")
# STEP 3
c.execute("SELECT * FROM Students")
# "SELECT * FROM employees WHERE last = 'Fernandes' 
# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM Students")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]

# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Database handling using MySQL on Cloud
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  yourdbname
MySQL username: yourusername
MySQL user password: dbpassword 
Email address:  your emailid
MYSQL URL : mysql://yourusername:dbpassword@db4free.net/yourdbname

"""


import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='himanshu_singh', password='himanshudb@8565',
                              host='db4free.net', database = 'himanshu_db')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("DROP Table Students;")

# STEP 3
c.execute ("""CREATE TABLE Students(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")

# STEP 4
c.execute("INSERT INTO Students VALUES ('Sylvester', 50, 1 , 'CSE')")
c.execute("INSERT INTO Students VALUES ('Yogendra', 40, 2 , 'IT')")
c.execute("INSERT INTO Students VALUES ('Pradeep', 30, 3 , 'ECE')")
c.execute("INSERT INTO Students VALUES ('Kunal', 30, 4 , 'ME')")
c.execute("INSERT INTO Students VALUES ('Devendra', 49, 5 , 'IT')")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM Students")


# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 6
df_mysql = DataFrame(c.fetchall())  # putting the result into Dataframe
df_mysql.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Latest Code for Mongo Atlas
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
# client = pymongo.MongoClient("mongodb://yourusername:dbpassword@cluster0-shard-00-00-tdcf5.mongodb.net:27017,cluster0-shard-00-01-tdcf5.mongodb.net:27017,cluster0-shard-00-02-tdcf5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

client = pymongo.MongoClient("mongodb://himanshu_singh:himanshudb%408565@cluster-hs-shard-00-00-nqxtg.mongodb.net:27017,cluster-hs-shard-00-01-nqxtg.mongodb.net:27017,cluster-hs-shard-00-02-nqxtg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-hs-shard-0&authSource=admin&retryWrites=true")


mydb = client.himanshu_db

def add_student(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.Students.insert_one(
            {
            "Student_Name" : Student_Name,
            "Student_Age" : Student_Age,
            "Student_Roll_no" : Student_Roll_no,
            "Student_Branch" : Student_Branch
            })
    return "Student added successfully"


def fetch_all_student():
    user = mydb.Students.find()
    for i in user:
        print (i)




add_student('Sylvester', 50, 1 , 'CSE')
add_student('Yogendra', 40, 2 , 'IT')
add_student('Pradeep', 30, 3 , 'ECE')
add_student('Kunal', 30, 4 , 'ME')
add_student('Devendra', 49, 5 , 'IT')

fetch_all_student()
