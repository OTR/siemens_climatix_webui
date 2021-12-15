"""

"""
from typing import NamedTuple

import pytest
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError

from config.settings import test_settings
from services import poll_web_server


AHU_IPS = test_settings.AHU_IPS
SIEMENS_USER = test_settings.SIEMENS_USER
SIEMENS_PASSWD = test_settings.SIEMENS_PASSWD


def test_wrong_ip() -> None:
    """
    A test for wrong or unreachable IP. Covers:
    `requests.exceptions.ConnectionError Failed to establish a new connection`
    """
    try:
        _resp = requests.get("http://192.168.222.222/")
    except ConnectionError as err:
        if "Failed to establish a new connection" in err.__str__():
            assert True  # FIXME: refactor it. Assert raising exception
        else:
            raise err


@pytest.mark.parametrize("item", AHU_IPS.values())
def test_auth_required(item: NamedTuple) -> None:
    """
    Test IPs of all AHU's. Try to make a request without `Basic Auth` header.
    Expect getting `Unauthorized response` status.
    """
    ip = item.IP
    resp = requests.get(f"http://{ip}/")
    assert resp is not None
    assert resp.reason == "Unauthorized"
    assert resp.status_code == 401


@pytest.mark.parametrize("item", AHU_IPS.values())
def test_wrong_auth_credentials(item: NamedTuple) -> None:
    """
    Test if basic auth passed on all hosts.

    {'Server': 'Keil-EWEB/2.1',
    'Content-type': 'text/html',
    'WWW-Authenticate': 'Basic realm= "Embedded WEB Server"',
    'Connection': 'close'}
    """
    ip = item.IP
    url = f"http://{ip}/"
    user = "WrongUser"
    expected = 'Basic realm= "Embedded WEB Server"'

    resp = requests.get(url, auth=HTTPBasicAuth(user, SIEMENS_PASSWD))
    assert resp.headers.get("WWW-Authenticate") == expected
    assert resp.status_code == 401


@pytest.mark.parametrize("item", AHU_IPS.values())
def test_auth_passed(item: NamedTuple) -> None:
    """Test if Basic Auth has passed on all hosts."""
    ip = item.IP
    url = f"http://{ip}/"

    resp = requests.get(url, auth=HTTPBasicAuth(SIEMENS_USER, SIEMENS_PASSWD))
    # E      - Wed, 01 Jan 2003 00:00:00 GMT
    # E      + Thu, 06 May 2021 14:29:16 GMT
    assert resp.headers.get("Last-Modified") is True
    assert resp.status_code == 200


def test_proof_simple_text_hist() -> None:
    """Test simple_text_hist method of PLCWebClient class."""
    my_sess = poll_web_server.PLCWebClient(ahu_id="F")
    my_sess.simple_text_hist()
