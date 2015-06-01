# Description
This module reads the temperature and hunidity from a DHT22 sensor attached
to a raspberry pi. In the future there will also be a hook for a BMP180
pressure sensor. The result is send to a REST interface which saves the data
from the sensors in a database.

#Configuration
The configiguration of the URL, user and pass as well as the pin for the DHT22
sensor can be found in recorder.conf.

The format must be:
```
[REST]
url=<URL>
user=<USERNAME>
pass=<PASSWORD>

[DHT22]
pin=<PIN>
```

#Usage
The script is executable and can be used directly

##Example
```
$ ./record_weather.py
```
or as a cronjob
```
0 *   * * *   root    /opt/weather/record_weather.py
```

#Note
In order to use the module you need to install:

* Adafruit_DHT
* json
* requests
