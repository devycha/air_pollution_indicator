from air_pollution import pm_value as pm
from lcd import msg, cleanup, error_msg
import led as led
import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
ROW = [6, 13, 19, 26]

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try: 
    pm_data = pm(0) # 처음 시작시 미세먼지 데이터를 받아온 뒤에 데이터값 저장

    # 4번 버튼을 Interrupt키로 지정, Interrupt 발생 시 미세먼지 데이터를 다시 받아오는 함수(pm()) 실행, 재입력방지는 1초로 설정
    GPIO.add_event_detect(19, GPIO.FALLING, callback=pm, bouncetime=1000)

    if pm_data['pm10_data']['grade'] != 'null' and pm_data['pm25_data']['grade'] != 'null':
        led.normal_led()
        
        while True:
            cleanup() # LCD Clean UP
            now = datetime.datetime.now()
            minute = str(now.minute)
            second = str(now.second)
            if (int(pm_data['pm10_data']['grade'] >= pm_data['pm25_data']['grade'])):
                pm_title = "pm_10"
                pm_grade = pm_data['pm10_data']['grade']
                pm_value = pm_data['pm10_data']['value']
            else:
                pm_title = "pm_2.5"
                pm_grade = pm_data['pm25_data']['grade']
                pm_value = pm_data['pm25_data']['value']

            if GPIO.input(13) == 0:
                pm_title = "SO2"
                pm_grade = pm_data['so2_data']['grade']
                pm_value = pm_data['so2_data']['value']
            elif GPIO.input(6) == 0:
                pm_title = "CO"
                pm_grade = pm_data['co_data']['grade']
                pm_value = pm_data['co_data']['value']
            elif GPIO.input(26) == 0:
                pm_title = "O3"
                pm_grade = pm_data['o3_data']['grade']
                pm_value = pm_data['o3_data']['value']
            
            msg(pm_title, pm_grade, pm_value)

            if pm_grade == '1':
                led.blue()
            elif pm_grade == '2':
                led.green()
            elif pm_grade == '3':
                led.yellow()
            elif pm_grade == '4':
                led.red()

            if (minute == "00" and second == "00"):
                pm_data = pm(0)

            time.sleep(1)
    else:
        while True:
            led.maintain_led()
            if GPIO.input(19) == 0:
                break
except:
    error_msg()
    cleanup()
    led.turnOff()