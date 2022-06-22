from unittest import mock
import pytest

from myapp.sample import guess_number, get_ip


# attach a decorator
@pytest.mark.parametrize('_input, expected', [(3, 'You won'), (4, 'You Lost')])
@mock.patch('myapp.sample.roll_dice')
def test_guest_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected 
    mock_roll_dice.assert_called_once()

# test get ip
@mock.patch('myapp.sample.requests.get')
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                               **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")


