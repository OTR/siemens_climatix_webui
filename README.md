### Installation

#### via Pip

```commandline
$ python -m venv webui_venv
$ cd webui_venv
(Windows) $ Scripts/Activate.bat
(Linux) $ . bin/activate
$ git clone https://github.com/OTR/siemens_climatix_webui.git webui
$ cd webui
$ pip install -r requirements.txt
$ python manage.py makemigrations
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

* Navbar covers content when expanding

* Move javascript from `index.html` pattern to separate `.js` file and import it
