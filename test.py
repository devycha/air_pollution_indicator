from air_pollution import pm_value as pm
from lcd import msg, cleanup, error_msg
import led2 as led
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
ROW = [6, 13, 19, 26]
# pin_1 = GPIO.input(13)
# pin_2 = GPIO.input(6)
# pin_3 = GPIO.input(26)
# pin_4 = GPIO.input(19)
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)


# while True:
#     # 초기화버튼 입력시 데이터 받아오기

pm_data = pm()
so2_data = {
    'grade': pm_data[0]['so2Grade'] if pm_data[0]['so2Grade'] else pm_data[1]['so2Grade'],
    'value': pm_data[0]['so2Value'] if pm_data[0]['so2Value'] else pm_data[1]['so2Value']
}

co_data = {
    'grade': pm_data[0]['coGrade'] if pm_data[0]['coGrade'] else pm_data[1]['coGrade'],
    'value': pm_data[0]['coValue'] if pm_data[0]['coValue'] else pm_data[1]['coValue']
}

o3_data = {
    'grade': pm_data[0]['o3Grade'] if pm_data[0]['o3Grade'] else pm_data[1]['o3Grade'],
    'value': pm_data[0]['o3Value'] if pm_data[0]['o3Value'] else pm_data[1]['o3Value']
}

pm10_data = {
    'grade': pm_data[0]['pm10Grade'] if pm_data[0]['pm10Grade'] else pm_data[1]['pm10Grade'],
    'value': pm_data[0]['pm10Value'] if pm_data[0]['pm10Value'] else pm_data[1]['pm10Value']
}

pm25_data = {
    'grade': pm_data[0]['pm25Grade'] if pm_data[0]['pm25Grade'] else pm_data[1]['pm25Grade'],
    'value': pm_data[0]['pm25Value'] if pm_data[0]['pm25Value'] else pm_data[1]['pm25Value']
}

if pm10_data['grade'] != 'null' and pm25_data['grade'] != 'null':
    led.normal_led()
    
    while True:
        cleanup() # LCD Clean UP
        if (int(pm10_data['grade'] >= pm25_data['grade'])):
            pm_title = "pm_10"
            pm_prev = "pm_10"
            pm_grade = pm10_data['grade']
            pm_value = pm10_data['value']
        else:
            pm_title = "pm_2.5"
            pm_prev = "pm_2.5"
            pm_grade = pm25_data['grade']
            pm_value = pm25_data['value']

        if GPIO.input(19) == 0:
            cleanup()
            led.turnOff()
            break
        elif GPIO.input(13) == 0:
            pm_title = "SO2"
            pm_grade = so2_data['grade']
            pm_value = so2_data['value']
        elif GPIO.input(6) == 0:
            pm_title = "CO"
            pm_grade = co_data['grade']
            pm_value = co_data['value']
        elif GPIO.input(26) == 0:
            pm_title = "O3"
            pm_grade = o3_data['grade']
            pm_value = o3_data['value']
        
        msg(pm_title, pm_grade, pm_value)

        if pm_grade == '1':
            led.blue()
        elif pm_grade == '2':
            led.green()
        elif pm_grade == '3':
            led.yellow()
        elif pm_grade == '4':
            led.red()

        time.sleep(1)
else:
    while True:
        led.maintain_led()
        if GPIO.input(19) == 0:
            break



# pm_grade = max(int(pm10_data['grade']), int(pm25_data['grade']))
# if pm_grade == 1:
#     led.blue()
# elif pm_grade == 2:
#     led.green()
# elif pm_grade == 3:
#     led.yellow()
# elif pm_grade == 4:
#     led.red()

# while True:
#     msg("pm_10.0", pm10_data['grade'], pm10_data['value'])
#     time.sleep(2)
#     msg("pm_2.50", pm25_data['grade'], pm25_data['value'])
#     time.sleep(2)
