import RPi.GPIO as GPIO # 라즈베리파이 GPIO 제어
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 

# 미세먼지 등급을 표시하는 LED (RGB-LED)
redPin = 11 # GPIO 11번 핀 = R
greenPin = 9 # GPIO 9번 핀 = G
bluePin = 10 # GPIO 10번 핀 = B

# 정상작동 여부를 표시하는 신호등 LED(RYG)
redPin2 = 17 # 
yellowPin = 27
greenPin2 = 22

# GPIO 핀을 OUTPUT으로 셋팅
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(redPin2,GPIO.OUT)
GPIO.setup(yellowPin,GPIO.OUT)
GPIO.setup(greenPin2,GPIO.OUT)

# 모든 LED를 OFF
def turnOff():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    GPIO.output(redPin2, GPIO.LOW)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(greenPin2, GPIO.LOW)

# RGB-LED를 흰색으로
def white():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

# RGB-LED를 빨간색(매우 나쁨 - 4)으로
def red():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)

# RGB-LED를 초록색(보통 - 2)으로
def green():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)

# RGB-LED를 파란색(좋음 - 1)으로
def blue():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)

# RGB-LED를 노란색(나쁨 - 3)으로
def yellow():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)

# 신호등-LED를 빨간색(알 수 없는 오류)으로
def error_led():
    GPIO.output(redPin2, GPIO.HIGH)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(greenPin2,GPIO.LOW)

# 신호등-LED를 노란색(점검 중)으로
def maintain_led():
    GPIO.output(redPin2, GPIO.LOW)
    GPIO.output(yellowPin,GPIO.HIGH)
    GPIO.output(greenPin2,GPIO.LOW)

# 신호등-LED를 초록색(정상 작동 중)으로
def normal_led():
    GPIO.output(redPin2, GPIO.LOW)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(greenPin2,GPIO.HIGH)

# 미세먼지 등급에 따라 LED 색 제어
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
    
