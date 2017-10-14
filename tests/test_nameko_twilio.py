from mock import Mock, patch, call

import pytest

from nameko_twilio import Twilio


@pytest.fixture
def mock_twilio_client():
    with patch('nameko_twilio.Client') as Client:
        yield Client


@pytest.fixture
def twilio_dependency():
    twilio = Twilio()
    twilio.container = Mock()
    twilio.container.config = {
        'account_sid': '123',
        'auth_token': 'ABC'
    }
    return twilio


def test_setup(twilio_dependency):
    twilio_dependency.setup()
    assert twilio_dependency.account_sid == '123'
    assert twilio_dependency.auth_token == 'ABC'


def test_start(mock_twilio_client, twilio_dependency):
    twilio_dependency.setup()
    twilio_dependency.start()
    assert mock_twilio_client.call_args_list == [call('123', 'ABC')]


def test_get_dependency(mock_twilio_client, twilio_dependency):
    twilio_dependency.setup()
    twilio_dependency.start()
    client = twilio_dependency.get_dependency(Mock())
    assert client == twilio_dependency.client


def test_stop(mock_twilio_client, twilio_dependency):
    twilio_dependency.setup()
    twilio_dependency.start()
    twilio_dependency.stop()
    assert twilio_dependency.client is None
