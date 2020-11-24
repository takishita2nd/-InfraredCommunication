import RPi.GPIO as GPIO
import time
import datetime

def __main__():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN)
    GPIO.add_event_detect(21, GPIO.BOTH, callback=callback)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

def callback(channel):
    print(str(GPIO.input(21)) + " " + datetime.datetime.now().isoformat())

__main__()

