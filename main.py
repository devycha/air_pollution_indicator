from air_pollution import pm_value as pm # 공공데이터 포털 한국환경공단 에어코리아의 실시간 미세먼지 정보 데이터 추출 API
from lcd import msg, cleanup, error_msg, wait_msg # 미세먼지 정보를 표시하는 LCD Display
import led as led # 정상 작동 여부와 미세먼지 정보를 표시하는 LED 제어
import time # 1시간마다 update를 하기 위한 time 모듈
import RPi.GPIO as GPIO # 라즈베리파이의 GPIO를 제어하기 위한 모듈

# 라즈베리파이 GPIO 셋 모드
GPIO.setmode(GPIO.BCM)

# 1번 버튼 GPIO.input(13)
# 2번 버튼 GPIO.input(6)
# 3번 버튼 GPIO.input(26)
# 4번 버튼 GPIO.input(19)
ROW = [6, 13, 19, 26]

# 버튼을 INPUT값으로 설정 버튼을 눌렀다 떼었을 때 값이 변경되도록 1번~4번 버튼 모두 설정
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)



while True:
    try:
        pm_data = pm3()
        print("PM Data is Updated!!")
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
        try:
            if pm10_data['grade'] != 'null' and pm25_data['grade'] != 'null':
                led.normal_led()
                
                while True:
                    cleanup() # LCD Clean Up
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
                        wait_msg()
                        led.turnOff()
                        time.sleep(1)
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

                    time.sleep(0.5)
            else:
                while True:
                    cleanup()
                    led.turnOff()
                    led.maintain_led()
                    if GPIO.input(19) == 0:
                        cleanup()
                        led.turnOff()
                        break
        except Exception as e:
            error_msg()
            led.error_led()
            break
    except:
        led.turnOff()
        error_msg()
        while True:
            led.error_led()
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
