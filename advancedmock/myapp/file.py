# making multiple calls to the obj we trying to call
# patching into a single unit test

import random
import time

import requests


def random_sum():
    # here we r not sure the output of this function
    a = random.randint(1, 10)
    b = random.randint(1, 7)
    return a + b


def silly():
    params = {
        "timestamp": time.time(),
        "number": random.randint(1, 6)
    }

    response = requests.get("https://httpbin.org/get", params)
    if response.status_code == 200:
        return response.json()['args']