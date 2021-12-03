from air_pollution import pm_value as pm
from lcd import msg, cleanup, error_msg, maintain_msg
from led import normal_led, maintain_led, error_led, turnOff, pm_led
import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
ROW = [6, 13, 19, 26]

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)



pm_data = pm()

def pm10(channel):
    pm_title = "pm_10"
    pm_grade = pm_data['pm10_data']['grade']
    pm_value = pm_data['pm10_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)

def pm25(channel):
    pm_title = "pm_2.5"
    pm_grade = pm_data['pm25_data']['grade']
    pm_value = pm_data['pm25_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)
    

def so2(channel):
    pm_title = "SO2"
    pm_grade = pm_data['pm25_data']['grade']
    pm_value = pm_data['pm25_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)
    

def co(channel):
    pm_title = "CO"
    pm_grade = pm_data['co_data']['grade']
    pm_value = pm_data['co_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)
    

def o3(channel):
    pm_title = "O3"
    pm_grade = pm_data['o3_data']['grade']
    pm_value = pm_data['o3_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)

pm10(0)

GPIO.add_event_detect(13, GPIO.FALLING, callback=pm10, bouncetime=2000)
GPIO.add_event_detect(6, GPIO.FALLING, callback=pm25, bouncetime=2000)
GPIO.add_event_detect(26, GPIO.FALLING, callback=co, bouncetime=2000)
GPIO.add_event_detect(19, GPIO.FALLING, callback=o3, bouncetime=2000)

try:
    while True:
        try:
            # cleanup()
            if pm_data['pm10_data']['grade'] != 'null' and pm_data['pm25_data']['grade'] != 'null':
                normal_led()
                now = datetime.datetime.now()
                minute = str(now.minute)
                second = str(now.second)
            else:
                maintain_msg()
                maintain_led()
            if (minute == "00" and second == "00"):
                    pm_data = pm()
                    pm10(0)
            
        except:
            error_msg()
            cleanup()
            error_led()
            time.sleep(1)
except:
    cleanup()
    turnOff()
    error_led()
