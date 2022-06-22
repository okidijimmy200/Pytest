import requests 
from .dice import roll_dice

def guess_number(num):
    result = roll_dice()
    if result == num:
        return 'You won'
    else:
        return 'You Lost'

# to get ip address of the computer
def get_ip():
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        return response.json()['origin']