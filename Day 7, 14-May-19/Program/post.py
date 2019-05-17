# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:09:52 2019

@author: HIMANSHU SINGH
"""

import json
import requests

Host = "https://eno2tz37xgzvp.x.pipedream.net/post"

data = {"firstname":"Himanshu","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

response = requests.post(Host,data,headers)
print(response.json()) 

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("https://eno2tz37xgzvp.x.pipedream.net/get?firstname=Himanshu&language=English")
    return response

print (get_method().text)