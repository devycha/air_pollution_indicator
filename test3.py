from air_pollution import pm_value as pm # 공공데이터 포털 한국환경공단 에어코리아의 실시간 미세먼지 정보 데이터 추출 API
from lcd import msg, cleanup, error_msg, maintain_msg # 미세먼지 정보를 표시하는 LCD Display
from led import normal_led, maintain_led, error_led, turnOff, pm_led # 정상 작동 여부와 미세먼지 정보를 표시하는 LED 제어
from mail import send_mail # 미세먼지 정보를 메일로 발송하기 위한 SMTP 모듈
import time # time.sleep을 이용하여 기기 오작동 방지
import RPi.GPIO as GPIO # 라즈베리파이의 GPIO를 제어하기 위한 모듈
import datetime # 1시간마다 update를 하기 위한 time 모듈

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


# 처음 기기가 켜졌을 때, 미세먼지 정보를 받아와서 pm_datg(전역변수)에 저장
pm_data = pm()

# 미세먼지 정보 데이터를 LCD에 표시하고 등급에 따라 LED 색 제어
def pm10(channel):
    pm_title = "pm_10"
    pm_grade = pm_data['pm10_data']['grade']
    pm_value = pm_data['pm10_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)

# 초미세먼지 정보 데이터를 LCD에 표시하고 등급에 따라 LED 색 제어
def pm25(channel):
    pm_title = "pm_2.5"
    pm_grade = pm_data['pm25_data']['grade']
    pm_value = pm_data['pm25_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)
    
# 이산화 황 정보 데이터를 LCD에 표시하고 등급에 따라 LED 색 제어
# 버튼을 4개밖에 추가하지 못하여 이산화 황 데이터는 사용하지 못했습니다.
def so2(channel):
    pm_title = "SO2"
    pm_grade = pm_data['pm25_data']['grade']
    pm_value = pm_data['pm25_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)
    
# 일산화탄소 정보 데이터를 LCD에 표시하고 등급에 따라 LED 색 제어
def co(channel):
    pm_title = "CO"
    pm_grade = pm_data['co_data']['grade']
    pm_value = pm_data['co_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)
    
# 오존 정보 데이터를 LCD에 표시하고 등급에 따라 LED 색 제어
def o3(channel):
    pm_title = "O3"
    pm_grade = pm_data['o3_data']['grade']
    pm_value = pm_data['o3_data']['value']
    msg(pm_title, pm_grade, pm_value)
    pm_led(pm_grade)

# 처음 시작 시 미세먼지 데이터를 기본적으로 LCD Display에 표시 
pm10(0)

# Interrupt 추가: 1번~4번 버튼을 Interrupt로 추가하여 발생시 
# callback함수로 각각의 오염물질 정보를 LCD와 LED에 표시하는 함수로 등록
# bouncetime을 2s로 지정하여 누르고있는 동안에 지속적으로 콜백함수가 반복되는 것을 방지
GPIO.add_event_detect(13, GPIO.FALLING, callback=pm10, bouncetime=2000)
GPIO.add_event_detect(6, GPIO.FALLING, callback=pm25, bouncetime=2000)
GPIO.add_event_detect(26, GPIO.FALLING, callback=co, bouncetime=2000)
GPIO.add_event_detect(19, GPIO.FALLING, callback=o3, bouncetime=2000)

# 오류 발생시 except로 이동
try:
    while True:
        try:
            # cleanup()
            if pm_data['pm10_data']['grade'] != 'null' and pm_data['pm25_data']['grade'] != 'null':
                normal_led()
                 
            else:
                maintain_msg() # LCD 디스플레이에 기기가 점검 중임을 표시
                maintain_led() # 한국환경 공단의 미세먼지 데이터가 null값이면 기기가 점검중이기 때문에 정상작동 LED를 노란색으로 ON

            # 현재 시간 정보를 받아옴.
            now = datetime.datetime.now()
            minute = str(now.minute)
            second = str(now.second)
            if (minute == "00" and second == "10"): 
            # ㅁㅁ시 10분이 됐을 때 미세먼지 정보를 업데이트하여 메일전송 후 미세먼지 정보를 LCD와 LED로 표시 
            # 미세먼지 정보가 보통 정각에 업데이트 되는 것을 확인하고 10분 정도의 시차를 두었음.
                    pm_data = pm() 
                    send_mail(pm_data)
                    pm10(0) 
                    
            
        except:
            error_msg() # LCD 디스플레이에 알수 없는 오류가 발생하였음을 표시
            error_led() # 정상작동 여부를 나타내는 신호등 LED를 빨간색으로 ON
            time.sleep(1) # 1초 지연
except:
    cleanup() # LCD 디스플레이의 정보 초기화
    turnOff() # 모든 LED OFF
    error_led() # 정상작동 LED를 빨간색으로 ON
