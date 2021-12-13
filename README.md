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
$ python manage.py migrate
$ python manage.py createsuperuser // (optional)
```

### Run test web server

Run the following command from droject directory

```commandline
$ python -m http.server --directory ./mock 8888
```

### Project structure

### TODO List

#### End points of the web site

`/` - display and dinamicly update (every second) current temperature and air volume values of air handling units (AHU)

`/admin` - default Django admin panel

`/list` - display a history (trends) of changing temperature and air volume of AHU's

`/latest` - return data that describes AHU's condition (air volume, temperature, relative humidity) in JSON representation, needed for XHR

`/crash_history` - display all crash records (alarms, warnings, faults, ...) i.e., logs for a certain AHU
