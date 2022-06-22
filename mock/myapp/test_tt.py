from unittest import mock
from .tt import Consumer
class TestConsumer:

    @mock.patch('path.to.Consumer')
    def test_should_check_for_updates_when_consumer_is_running(
        self,
        service_mock
    ):

        sentinel = mock.PropertyMock(side_effect=[True, False])
        Consumer.RUNNING = sentinel

        my_consumer = Consumer(service_mock)
        my_consumer.start()

        service_mock.check_for_updates.assert_called()
        assert service_mock.check_for_updates.call_count == 1  # called only once because on the second lap RUNNING is False