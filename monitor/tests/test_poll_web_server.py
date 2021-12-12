"""

"""
import pytest
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError

from services import poll_web_server


def test_wrong_ip():
    """
    A test for wrong or unreachable IP. Covers:
    `requests.exceptions.ConnectionError Failed to establish a new connection`
    """
    try:
        resp = requests.get("http://192.168.222.222/")
    except ConnectionError as err:
        if "Failed to establish a new connection" in err.__str__():
            assert True  # FIXME: refactor it. Assert catching exception
        else:
            raise err


@pytest.mark.parametrize("item", poll_web_server.AHU_IPS["hosts"].items())
def test_auth_required(item):
    """
    Test IPs of all AHU's. Try to make a request without `Basic Auth` header.
    Expect getting `Unauthorized response` status.
    """
    ip = item[1]
    resp = requests.get(f"http://{ip}/")
    assert resp is not None
    assert resp.reason == "Unauthorized"
    assert resp.status_code == 401


@pytest.mark.parametrize("item", poll_web_server.AHU_IPS["hosts"].items())
def test_wrong_auth_credentials(item):
    """
    Test if basic auth passed on all hosts.

    {'Server': 'Keil-EWEB/2.1',
    'Content-type': 'text/html',
    'WWW-Authenticate': 'Basic realm= "Embedded WEB Server"',
    'Connection': 'close'}
    """
    url = f"http://{item[1]}/"
    user = "WrongUser"
    passwd = poll_web_server.SIEMENS_PASSWD
    expected = 'Basic realm= "Embedded WEB Server"'

    resp = requests.get(url, auth=HTTPBasicAuth(user, passwd))
    assert resp.headers.get("WWW-Authenticate") == expected
    assert resp.status_code == 401


@pytest.mark.parametrize("item", poll_web_server.AHU_IPS["hosts"].items())
def test_auth_passed(item):
    """Test if Basic Auth has passed on all hosts."""
    url = f"http://{item[1]}/"
    user = poll_web_server.SIEMENS_USER
    passwd = poll_web_server.SIEMENS_PASSWD

    resp = requests.get(url, auth=HTTPBasicAuth(user, passwd))
    # E      - Wed, 01 Jan 2003 00:00:00 GMT
    # E      + Thu, 06 May 2021 14:29:16 GMT
    assert resp.headers.get("Last-Modified") is True
    assert resp.status_code == 200


def test_proof_simple_text_hist():
    """Test simple_text_hist method of PLCWebClient class."""
    my_sess = poll_web_server.PLCWebClient(_id="1.1")
    my_sess.simple_text_hist()
