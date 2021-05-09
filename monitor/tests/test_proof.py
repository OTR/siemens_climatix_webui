import pytest
import requests
from requests.exceptions import ConnectionError
from requests.auth import HTTPBasicAuth

from scripts import proof


def test_wrong_ip():
	"""Test for wrong or unreachable IP
	requests.exceptions.ConnectionError
	Failed to establish a new connection"""
	try:
		resp = requests.get("http://192.168.222.222/")
	except ConnectionError as e:
		if "Failed to establish a new connection" in e.__str__():
			assert True  # FIXME: refactor it. Assert catching exception
		else:
			raise e


@pytest.mark.parametrize("item", proof.CONFIG["hosts"].items())
def test_auth_required(item):
	"""Test IPs of CVU's"""
	ip = item[1]
	resp = requests.get(f"http://{ip}/")
	assert resp is not None
	# Try out without Basic Auth
	# Expect getting Unauthorized response
	assert resp.reason == "Unauthorized"
	assert resp.status_code == 401


@pytest.mark.parametrize("item", proof.CONFIG["hosts"].items())
def test_wrong_auth_credentials(item):
	"""Test if basic auth passed on all hosts

	{'Server': 'Keil-EWEB/2.1',
	'Content-type': 'text/html',
	'WWW-Authenticate': 'Basic realm= "Embedded WEB Server"',
	'Connection': 'close'}"""
	url = f"http://{item[1]}/"
	user = "WrongUser"
	passwd = proof.passwd

	resp = requests.get(url, auth=HTTPBasicAuth(user, passwd))
	assert resp.headers.get("WWW-Authenticate") == 'Basic realm= "Embedded WEB Server"'
	assert resp.status_code == 401


@pytest.mark.parametrize("item", proof.CONFIG["hosts"].items())
def test_auth_passed(item):
	"""Test if basic auth passed on all hosts"""
	url = f"http://{item[1]}/"
	user = proof.user
	passwd = proof.passwd

	resp = requests.get(url, auth=HTTPBasicAuth(user, passwd))
	# E      - Wed, 01 Jan 2003 00:00:00 GMT
	# E      + Thu, 06 May 2021 14:29:16 GMT
	assert resp.headers.get("Last-Modified") is True
	assert resp.status_code == 200

def test_proof_simple_text_hist():
	"""Test simple_text_hist method of MySession class"""
	my_sess = proof.MySession(_id="1.1")
	my_sess.simple_text_hist()
