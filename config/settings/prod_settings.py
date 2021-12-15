"""
Django settings for production.
"""
from collections import namedtuple

from .common_settings import *

AHU_ip_by_name = namedtuple("AHU", "IP name")

ALLOWED_HOSTS = ["127.0.0.1"]
AHU_PORT = 80

# Identifier as single character, IP address, verbose name
AHU_IPS = {
    "0": AHU_ip_by_name("169.254.188.220", "1.1"),
    "1": AHU_ip_by_name("169.254.130.48", "1.2"),
    "2": AHU_ip_by_name("169.254.1.28", "1.3"),
    "3": AHU_ip_by_name("169.254.1.42", "1.4"),
    "4": AHU_ip_by_name("169.254.97.128", "2.1"),
    "5": AHU_ip_by_name("169.254.53.139", "2.2"),
    "6": AHU_ip_by_name("169.254.45.14", "2.3"),
    "7": AHU_ip_by_name("169.254.58.171", "2.4"),
    "8": AHU_ip_by_name("169.254.157.21", "3.1"),
    "9": AHU_ip_by_name("169.254.2.251", "3.2"),
    "A": AHU_ip_by_name("169.254.164.35", "3.3"),
    "B": AHU_ip_by_name("169.254.154.250", "3.4"),
    "C": AHU_ip_by_name("169.254.154.245", "4.1"),
    "D": AHU_ip_by_name("169.254.242.245", "4.2"),
    "E": AHU_ip_by_name("169.254.56.35", "4.3"),
    "F": AHU_ip_by_name("169.254.252.44", "4.4"),
}

# FIXME: os.environ["HOME"] or os.environ["%USERPROFILE%"]
#  %APPDATA%, distinguish between app logs and AHU history logs
AHU_HISTORY_DIR = BASE_DIR / "logs"

# No worries it is standard credentials, no leaking here
SIEMENS_USER = "WEB"
SIEMENS_PASSWD = "SBTAdmin!"
