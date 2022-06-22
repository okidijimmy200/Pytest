from unittest import mock
import pytest
from delivery.chat import delivery_report
# def delivery_report(err, msg):
#     # to indicate err incase any
#     if err is not None:
#         x = 'Message delivery failed: {}'.format(err)
#         return x
#     # to indicate delivery message 
#     else:
#         y = 'Message delivered to {} [{}]'.format(msg.topic(), msg.partition())
#         return y


# # print(delivery_report(err='error msg', msg='message'))

# # creating a mock class
# # mock_roll_dice = mock.Mock(name='roll dice mock') # name is optional and its used for debugging
# #  to return a given value
# mock_delivery_report = mock.Mock(name='delivery report', return_value='Message delivery failed: error msg')

# # print(mock_delivery_report())

# # # how to assign roll_dice to mock_roll_dice
# delivery_report = mock_delivery_report
# print(delivery_report())


def test_delivery_report():
    mock_delivery_report = mock.Mock(name='delivery report', return_value='Message delivery failed: error msg')
    delivery_report = mock_delivery_report
    assert delivery_report(err='error msg', msg='message') == 'Message delivery failed: error msg'

