"""
Django settings for testing.
"""
from collections import namedtuple

from .common_settings import *

AHU_ip_by_name = namedtuple("AHU", "IP name")

ALLOWED_HOSTS = ["127.0.0.1"]
DEBUG = True
AHU_PORT = 8888
AHU_IPS = {
    "0": AHU_ip_by_name("127.0.0.1", "1.1"),
    "1": AHU_ip_by_name("127.0.0.1", "1.2"),
    "2": AHU_ip_by_name("127.0.0.1", "1.3"),
    "3": AHU_ip_by_name("127.0.0.1", "1.4"),
    "4": AHU_ip_by_name("127.0.0.1", "2.1"),
    "5": AHU_ip_by_name("127.0.0.1", "2.2"),
    "6": AHU_ip_by_name("127.0.0.1", "2.3"),
    "7": AHU_ip_by_name("127.0.0.1", "2.4"),
    "8": AHU_ip_by_name("127.0.0.1", "3.1"),
    "9": AHU_ip_by_name("127.0.0.1", "3.2"),
    "A": AHU_ip_by_name("127.0.0.1", "3.3"),
    "B": AHU_ip_by_name("127.0.0.1", "3.4"),
    "C": AHU_ip_by_name("127.0.0.1", "4.1"),
    "D": AHU_ip_by_name("127.0.0.1", "4.2"),
    "E": AHU_ip_by_name("127.0.0.1", "4.3"),
    "F": AHU_ip_by_name("127.0.0.1", "4.4"),
}

# FIXME: os.environ["HOME"] or os.environ["%USERPROFILE%"]
#  %APPDATA%, distinguish between app logs and AHU history logs
AHU_HISTORY_DIR = BASE_DIR / "logs"

SIEMENS_USER = ""
SIEMENS_PASSWD = ""
