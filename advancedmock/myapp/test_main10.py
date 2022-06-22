# from subprocess import call
# from unittest import mock

# m = mock.Mock()

# # m.return_value = 3


# # we can specify a fun c to be called when a side effect is called
# # def my_side_effect(num):
# #     return num + 1
# # if we want ti return a different value different times
# # we use side effect
# # m.side_effect = [1,2,3, ZeroDivisionError()] # we can specify an exception

# def my_side_effect(num1, num2):
#     return num1 + num2

# m.side_effect = my_side_effect
# print(m(1, 5))

# # to call args
# m.call_args_list
# [call(1, 4), call(1, 5)]

# m.assert_has_calls([mock.call(1,4), mock.call(1,5)])