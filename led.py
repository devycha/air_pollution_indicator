#libraries
import RPi.GPIO as GPIO
from time import sleep
#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 11
greenPin = 9
bluePin = 10

redPin2 = 17
yellowPin = 27
greenPin2 = 22
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(redPin2,GPIO.OUT)
GPIO.setup(yellowPin,GPIO.OUT)
GPIO.setup(greenPin2,GPIO.OUT)

def turnOff():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    GPIO.output(redPin2, GPIO.LOW)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(greenPin2, GPIO.LOW)

def white():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def red():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)

def green():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def blue():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def yellow():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)

def error_led():
    GPIO.output(redPin2, GPIO.HIGH)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(greenPin2,GPIO.LOW)

def maintain_led():
    GPIO.output(redPin2, GPIO.LOW)
    GPIO.output(yellowPin,GPIO.HIGH)
    GPIO.output(greenPin2,GPIO.LOW)

def normal_led():
    GPIO.output(redPin2, GPIO.LOW)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(greenPin2,GPIO.HIGH)
    
def pm_led(grade):
    if grade == '1':
        blue()
    elif grade == '2':
        green()
    elif grade == '3':
        yellow()
    elif grade == '4':
        red()
    else:
        white()

turnOff()
    
