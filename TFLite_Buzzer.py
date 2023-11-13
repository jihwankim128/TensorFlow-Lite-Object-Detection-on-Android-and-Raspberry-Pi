import RPi.GPIO as GPIO

A_BUZ_PIN = 0
modelList = ["bus", "train", "bicycle", "car", "stop sign"]
GPIO.setmode(GPIO.BCM)
GPIO.setup(A_BUZ_PIN, GPIO.OUT)

def isVehicle(args):
    if args in modelList:
        GPIO.output(A_BUZ_PIN, GPIO.HIGH)
    else:
        GPIO.output(A_BUZ_PIN, GPIO.LOW)
