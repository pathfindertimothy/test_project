import requests
import os, sys
sys.path.append("")
from dotenv import load_dotenv
from payload.payload import *

load_dotenv()

# Add the url in the env file
# create a data file for payload

def get_single_product(num):
    # As a user I should be able to fetch a single product successfully
    url = 'https://fakestoreapi.com/products/' + str(num)
    resp = requests.get(url)
    resp_payload = resp.json()
    status = resp.status_code
    print(resp_payload)
    print("----------------------")
    print(status)
   
    my_value = resp_payload['price']
    print(my_value)
    # assert the status code in the test file
    # assert the price value in the test
# get_single_product()

def get_all_products():
    # As a user I should be able to fetch all product successfully
    url = 'https://fakestoreapi.com/products'
    resp = requests.get(url)
    resp_payload = resp.json()
    print(resp_payload)
    # assert the 2 and the 19 object title and price
# get_all_products()

def get_prodcut_by_count(num):
    # As a user I want to be able to get a specific number of products
    # note: I need a randon number generator for the num values
    url =  os.getenv('URL') + "?limit=" + str(num)
    resp = requests.get(url)
    resp_payload = resp.json()
    print(resp_payload)
    print(len(resp_payload))

    # assert that the count of the product is correct
    # assert status is correct
#get_prodcut_by_count(2)

def get_all_categories():
    # As a user, I want to be able to fetch all categories
    url =  os.getenv('URL') + "/categories"
    resp = requests.get(url)
    resp_payload = resp.json()
    print(resp_payload)
    print(len(resp_payload))
    # assert some of the category
    # assert the total number of category is 4
# get_all_categories()

def add_new_product():
    # As a user, I want to be able to add a new product
    url =  os.getenv('URL')
    resp = requests.post(url, data=new_product_payload)
    resp_payload = resp.json()
    print(resp_payload)
    print(len(resp_payload))
    print(resp.status_code)
    # assert the lenght of the dictionary
    # assert some value in the response
    # perform a get request to get the added product
    # assert the status code
# add_new_product()

def update_product():
    # As a user, I want to be able to update a product
    url =  os.getenv('URL') + '/' + str(7)
    resp = requests.put(url, data=put_payload)
    resp_payload = resp.json()
    print(resp_payload)
    print(len(resp_payload))
    print(resp.status_code)

update_product()

# add negative test such as adding a product with wrong category code or some wrong key
# add a negative test by passing wrong key so see how the system behave





