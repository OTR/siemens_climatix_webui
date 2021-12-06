### Description

A simple dynamic web site (built with Django, Bootstrap, XHR) that polls out data from builtin PLC's web server via Ethernet.

Full product name of PLC is: `Siemens Climatix POL638.00/STD`

### Installation

#### via Pip
```
$ python -m venv webui_venv
$ cd webui_venv
(Linux) $ source bin/activate
(Windows) $ Scripts\activate.bat
$ git clone https://github.com/OTR/siemens_climatix_webui.git webui
$ cd webui
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser // (optional, used for django's admin tool)
$ python manage.py runserver

Then open http://127.0.0.1/ in a Web browser
```

#### End points of the web site

`/` - display and dinamicly update (every second) current temperature and air volume values of air handling units (AHU)

`/admin` - default Django admin panel

`/list` - display a history (trends) of changing temperature and air volume of AHU's

`/latest` - return data that describes AHU's condition (air volume, temperature, relative humidity) in JSON representation, needed for XHR

`/crash_history` - display all crash records (alarms, warnings, faults, ...) i.e., logs for a certain AHU

#### Django's dependencies

```
asgiref	== 3.3.4
certifi	== 2020.12.5
chardet	== 4.0.0
Django == 3.2
h11 == 0.12.0
httpcore == 0.12.3
httpx == 0.17.1
idna == 2.10
lxml == 4.6.3
pip == 20.2.3
pytz == 2021.1
requests == 2.25.1
rfc3986	== 1.4.0
setuptools == 49.2.1
sniffio	== 1.2.0
sqlparse == 0.4.1
urllib3	== 1.26.4
```
