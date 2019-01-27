from mqtt import MQTTClient
import pycom
import sys
import time
import json
import ufun

from pysense import Pysense
from SI7006A20 import SI7006A20
import pycom
import micropython
import machine
import time





class Pycom:

    def flash_led(self, duration):
        pass

class LOG:
    def __init__(self, log_file = "log/log.dat"):
        self._log_file = log_file

    '''
    Log message to console with Info prefix


    message: message to display on console
    '''
    def log_info_console(message):
        pass
    '''
    Log error messages to the console with a Error prifix

    message: message to log
    '''
    def log_error_console(self, message):
        pass

    '''
    This method logs the data  to the file with the prifix Log specified during the creation of the object

    message: message to log to file
    '''

    def log_info_to_file(self, message):
        pass


    '''
    This method logs the data to the file with the prifix Error specified during the creation of the object

    message: message to log to file
    '''


    def log_error_to_file(self, message):
        pass

class ShowerPatrol:
    '''

    log_frequency: period for how often the sensor data is read. Should be given in seconds


    '''
    def __init__(self, log_frequency):

        self._log_frequency = log_frequency
        self.py = Pysense()
        self.tempHum = SI7006A20(py)
        self.temp_s = SI7006A20(py)

    def set_log_frequency(self, log_frequency):
        this._log_frequency = log_frequency

    def set_log_frequency(self, log_frequency):
        return this._log_frequency

    def start(self):
        while True:

            temperature = tempHum.temperature()
            print("Temperature: " + str(temp_s.temperature())+ " deg C and Relative Humidity: " + str(temp_s.humidity()) + " %RH")
            time.sleep(1)

while True:
    temperature = tempHum.temperature()
    print("Temperature: " + str(temp_s.temperature())+ " deg C and Relative Humidity: " + str(temp_s.humidity()) + " %RH")
    print("Dew point: "+ str(temp_s.dew_point()) + " deg C")


    time.sleep(1)
