import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

# pump pin number
pump_pin = 21
GPIO.setup(pump_pin, GPIO.OUT)

# humidity sensor
hum_pin = 26
GPIO.setup(hum_pin, GPIO.IN)


def pump(state):
    if not state:
        GPIO.output(pump_pin, GPIO.HIGH)
    else:
        GPIO.output(pump_pin, GPIO.LOW)


def is_humid():
    if GPIO.input(hum_pin):
        return 0
    else:
        return 1

