import requests
import os, sys
sys.path.append("")
from dotenv import load_dotenv
from payload.payload import *

load_dotenv()

def get_single_product():   
    url = os.getenv("URL") + "/" + str(1)

    try:
        resp = requests.get(url)
    except:
        print("Something went wrong")
    
    return resp

def get_all_products():
   
    url = os.getenv("URL")

    try:
        resp = requests.get(url)
    except:
        print("Something went wrong")
    
    return resp

def get_product_by_count(num):
    url =  os.getenv("URL") + "?limit=" + str(num)

    try:
        resp = requests.get(url)
    except:
        print("Something went wrong")
    
    return resp

def get_all_categories():
    url =  os.getenv("URL") + "/" + "categories"

    try:
        resp = requests.get(url)
    except:
        print("Something went wrong")
    
    return resp

def add_new_product():
    url =  os.getenv("URL")

    try:
        resp = requests.post(url, data=new_product_payload)
    except:
        print("Something went wrong")

    return resp

def update_product():
    url =  os.getenv("URL") + "/" + str(7)

    try:
        resp = requests.put(url, data=put_payload)
    except:
        print("Something went wrong")

    return resp

def get_product_by_catetory():
    url = os.getenv("URL") + "/" + "category" + "/" + "jewelery"

    try:
        resp = requests.get(url)
    except:
        print("Something went wrong")

    return resp

# Note: below endpoint returned only id
def add_user():
   

    url = os.getenv("USER_URL")

    try:
        resp = requests.post(url, data=new_user_payload)
    except:
        print("Something went wrong")

    return resp

def update_user():

    url = os.getenv("USER_URL") + "/" + str(7)

    try:
        resp = requests.patch(url, data=update_user_payload)
    except:
        print("Something went wrong")
    
    return resp

def user_login():
    url = os.getenv("LOGIN_URL")

    try:
        resp = requests.post(url, data=login_payload)
    except:
        print("Something went wrong")
    
    return resp