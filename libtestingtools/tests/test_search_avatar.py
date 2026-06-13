from libtestingtools import api_github
from unittest.mock import Mock
from requests.exceptions import HTTPError, ConnectionError, Timeout
import pytest


@pytest.fixture
def avatar_url(mocker):
    ans_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/116420402?v=4'
    ans_mock.json.return_value = {
        "login": "lucasfmerino",
        "id": 116420402,
        "node_id": "U_kgDOBvBvMg",
        "avatar_url": url,
    }
    ans_mock.raise_for_status = Mock()
    get_mock = mocker.patch('libtestingtools.api_github.requests.get')
    get_mock.return_value = ans_mock
    return url


def test_search_avatar(avatar_url):
    url = api_github.search_avatar("lucasfmerino")
    assert avatar_url == url


def test_search_avatar_integration():
    url = api_github.search_avatar("lucasfmerino")
    assert 'https://avatars.githubusercontent.com/u/116420402?v=4' == url


def test_search_avatar_http_error(mocker):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = HTTPError("404 Not Found")
    get_mock = mocker.patch('libtestingtools.api_github.requests.get')
    get_mock.return_value = mock_response
    with pytest.raises(HTTPError):
        api_github.search_avatar("nonexistent_user_12345")


def test_search_avatar_connection_error(mocker):
    get_mock = mocker.patch('libtestingtools.api_github.requests.get')
    get_mock.side_effect = ConnectionError("No connection")
    with pytest.raises(ConnectionError):
        api_github.search_avatar("lucasfmerino")


def test_search_avatar_timeout(mocker):
    get_mock = mocker.patch('libtestingtools.api_github.requests.get')
    get_mock.side_effect = Timeout("Request timed out")
    with pytest.raises(Timeout):
        api_github.search_avatar("lucasfmerino")
