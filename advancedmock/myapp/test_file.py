
from unittest import mock
from unittest.mock import call
from .file import random_sum, silly

@mock.patch('myapp.file.random.randint')
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls=[call(1, 10), call(1, 7)])

@mock.patch('myapp.file.random.randint')
@mock.patch('myapp.file.time.time')
@mock.patch('myapp.file.requests.get')
def test_silly(mock_requests_get, mock_time, mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params['timestamp']
    mock_randint.return_value = 5
    mock_requests_get.return_value = mock.Mock(**{"status_code": 200, "json.return_value": {"args": test_params}})

    assert silly() == test_params