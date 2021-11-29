import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ROW = [6, 13, 19, 26]

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# pin_1 = GPIO.input(13)
# pin_2 = GPIO.input(6)
# pin_3 = GPIO.input(26)
# pin_4 = GPIO.input(19)


while True:
    print(GPIO.input(6), GPIO.input(13), GPIO.input(19), GPIO.input(26))
    # print(pin_1, pin_2, pin_3, pin_4)
    time.sleep(1)
