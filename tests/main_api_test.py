import sys
sys.path.append("")

from func_api.api import *
from payload.payload import *

number_of_product = 2
payload_desc = put_payload['description']
payload_price = put_payload['price']
new_product_title = new_product_payload['title']
new_prodcut_cat = new_product_payload['category']
updated_email = update_user_payload['email']
updated_username = update_user_payload['username']

# - As a user I should be able to fetch a single product successfully
def test_get_single_product():
    resp = get_single_product()
    status = resp.status_code
    resp_payload = resp.json()
    price = resp_payload['price']
    title = resp_payload['title']

    assert status == 200
    assert price == 109.95
    assert title == 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops'
    assert 'price' in resp_payload
    assert 'title' in resp_payload

# - As a user I should be able to fetch all product successfully
def test_get_all_products():
    resp = get_all_products()
    status = resp.status_code
    resp_payload = resp.json()
    cat_one = resp_payload[2]['category']
    cat_two = resp_payload[19]['category']

    assert status == 200
    assert cat_one == "men's clothing"
    assert cat_two == "women's clothing"

# - As a user I want to be able to get a specific number of products
def test_get_prodcut_by_count():
    resp = get_product_by_count(number_of_product)
    status = resp.status_code
    resp_payload = resp.json()
    item_length = len(resp_payload)

    assert status == 200
    assert item_length == number_of_product

# - As a user, I want to be able to fetch all categories
def test_get_all_categories():
    resp = get_all_categories()
    status = resp.status_code
    resp_payload = resp.json()
    item_one = resp_payload[0]
    item_two = resp_payload[1]

    assert status == 200
    assert item_one == 'electronics'
    assert item_two == 'jewelery'

# - As a user, I want to be able to add a new product
def test_add_new_product():
    resp = add_new_product()
    status = resp.status_code
    resp_payload = resp.json()
    title = resp_payload['title']
    category = resp_payload['category']

    assert status == 200
    assert title == new_product_title
    assert category == new_prodcut_cat

# - As a user, I want to be able to update a product
def test_update_product():
    resp = update_product()
    status = resp.status_code
    resp_payload = resp.json()
    price = resp_payload['price']
    disc = resp_payload['description']

    assert status == 200
    assert 'description' in resp_payload
    assert price == str(payload_price)
    assert disc == payload_desc

# - As a user, I want to be able to get product in certain category
def test_get_product_by_catetory():
    resp = get_product_by_catetory()
    status = resp.status_code
    resp_payload = resp.json()
    cat_one = resp_payload[0]['category']
    cat_two = resp_payload[1]['category']
    rate = resp_payload[0]['rating']['rate']

    assert status == 200
    assert cat_one == 'jewelery'
    assert cat_two == 'jewelery'
    assert rate == 4.6

# As an admin, I should be able to create a new user
# Note: endpoint returned only an id in the payload 
def test_add_user():
    resp = add_user()
    status = resp.status_code
    resp_payload = resp.json()

    assert status == 200
    assert 'id' in resp_payload

# As an admin, I should be able to update a user
def test_update_user():
    resp = update_user()
    status = resp.status_code
    resp_payload = resp.json()
    email = resp_payload['email']
    username = resp_payload['username']

    assert status == 200
    assert email == updated_email
    assert username == updated_username
    assert 'email' in resp_payload

# As a user, I should be able to login successfully
def test_user_login():
    resp = user_login()
    status = resp.status_code
    resp_payload = resp.json()

    assert status == 200
    assert 'token' in resp_payload
