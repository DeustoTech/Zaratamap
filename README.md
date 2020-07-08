# Zaratamap
:busts_in_silhouette: [Amaia Goñi Ardanaz](https://www.linkedin.com/in/amaia-go%C3%B1i-ardanaz)

Ubiquitous sonometer with octave band analysis and web service for dynamic noise map creation.

### Execution instructions

#### Ubiquitous sonometer
Transfer the code building and loading it into the STM32F401RE using Keil uVision V5. The project is in Zaratamap\Industrial Electronics and Automation Engineering\Sonometer code (Keil)\zaratamap

#### InfluxDB database
Create an InfluxDB database manually, and populate it using the ubiquitous sonometer. Configure its name in the sonometer's config.h file.

#### Web service
Install the dependencies:
```sh
$ pip install -r requirements.txt
```

Run the Django migrations:
```sh
$ python manage.py makemigrations
$ python manage.py makemigrations polls
$ python manage.py migrate
```

Start the local web server:
```sh
$ python manage.py runserver
```

In the browser go to http://localhost:8000/

#### Machine learning application
Run the python scripts in Zaratamap\Computer Engineering\Machine Learning and datasets

#### OpenLayers map creation
Projects can be found in Zaratamap\Computer Engineering\Web service\GIS Features - Map development. Further instructions on their execution are included in Zaratamap\Documentation\INF_Amaia_Goñi_Ardanaz.pdf