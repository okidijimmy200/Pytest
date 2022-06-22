# from unittest import mock
# import random

# def roll_dice():
#     print('rolling...')
#     return random.randint(1, 6)

# # print(roll_dice())

# # creating a mock class
# # mock_roll_dice = mock.Mock(name='roll dice mock') # name is optional and its used for debugging
# #  to return a given value
# mock_roll_dice = mock.Mock(name='roll dice mock', return_value=3)

# # print(mock_roll_dice())

# # how to assign roll_dice to mock_roll_dice
# roll_dice = mock_roll_dice
# roll_dice()
# # print(roll_dice())

# # to check the number of times the mocks r called(there r multiple assertion methods)
# mock_roll_dice.assert_called_once()

# # how to determine when to use mock_roll_dice instead of real func
# # use patch to specify obj to mock

from unittest import mock
import requests

def get_ip():
    response = requests.get('http://httpbin.org/ip')
    if response.status_code == 200:
        return response.json()['origin']

get_ip()
# mock response object(we can pass properties as kwargs)
# mock_response = mock.Mock(return_value=2, status_code=200)
# we cls use dict unpacking
mock_response = mock.Mock(name="mock response",**{"status_code": 200, "json.return_value": "origin': '0.0.0.0"})

# json object inside mock function
# mock_response.json.return_value = {'origin': '0.0.0.0'}
# mock_response.status_code = 200

print(mock_response.json())

# mock request objects

mock_requests_get = mock.Mock(return_value=mock_response)

mock_requests_get().json # gives us the json response
mock_requests_get().status_code #gives us the status code
mock_requests_get.assert_called_once() # and other assert functions

# specify 
requests.get = mock_requests_get