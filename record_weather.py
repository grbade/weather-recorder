#!/usr/bin/python
"""record_weather.py

This module reads the temperature and hunidity from a DHT22 sensor attached
to a raspberry pi. In the future there will also be a hook for a BMP180
pressure sensor. The result is send to a REST interface which saves the data
from the sensors in a database.

The configiguration of the URL, user and pass as well as the pin for the DHT22
seonsor can be found in recorder.conf.

The format must be:

    [REST]
    url=<URL>
    user=<USERNAME>
    pass=<PASSWORD>

    [DHT22]
    pin=<PIN>

The script is executable and can be used directly

Example:
      $ ./record_weather.py

      or as a cronjob

      0 *   * * *   root    /opt/weather/record_weather.py

Note:
    In order to use the module you need to install:
    Adafruit_DHT
    json
    requests
"""

import Adafruit_DHT
import json
import requests
import ConfigParser, os


def record_weather():
    """The weather recording and post function

    Args:
        None

    Returns:
        True if successful, False otherwise.

    """
    #Getting the config file
    config = ConfigParser.ConfigParser()
    config.readfp(open('recorder.conf'))

    sensor = Adafruit_DHT.DHT22
    pin = config.get('DHT22', 'pin')

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #pressure sensor is not working yet so static value for now
    pressure = 1013.0

    try:
        #sending json msg containning the messured data to the REST interface
        url = config.get('REST', 'url')
        user = config.get('REST', 'user')
        passw = config.get('REST', 'pass')
        payload = {'pressure': pressure, 'temperature': temperature, 
                'humidity': humidity}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload),
                auth=(user, passw), headers=headers)
        if r.code == 200:
            return True
        else:
            return False
    except Exception, e:
        return False

if __name__ == "__main__":
    record_weather()
