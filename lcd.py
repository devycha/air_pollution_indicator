import I2C_LCD_driver
import time

# LCD Display를 제어할 수 있는 i2c bus (오픈소스 이용)
mylcd = I2C_LCD_driver.lcd()

# 미세먼지 정보를 파라미터로 입력받아 LCD에 표시
def msg(title, grade, value):
    mylcd.lcd_display_string(title)
    mylcd.lcd_display_string("Grade: " + grade, 2, 3)
    mylcd.lcd_display_string("Value: " + value, 3, 3)

# LCD Display의 글자를 모두 지움    
def cleanup():
    mylcd.lcd_clear()

# LCD Display에 알 수 없는 오류라는 정보를 표시
def error_msg():
    cleanup()
    mylcd.lcd_display_string('Unexpected Error is Occurred')

# LCD Display에 정보가 업데이트 중임을 표시
def wait_msg():
    cleanup()
    mylcd.lcd_display_string('Please wait for updating data')

# LCD Display에 기기가 점검 중임을 표시
def maintain_msg():
    cleanup()
    mylcd.lcd_display_string('The equipment is under inspection for a while')

# 모듈을 main에서 불러올 때 글자를 모두 지우고 시작
cleanup()
#Test1
# while True:
#    mylcd.lcd_display_string("미세먼지 농도", 1)
#    mylcd.lcd_display_string("Dreamming!!", 2, 3)
#    time.sleep(1)
#    mylcd.lcd_clear()
#    time.sleep(1)


#Test2
#while True:
#    mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
#    mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)


#Test3
#str_pad = " " * 16
#my_long_string = "Thank for subscribe the DeveloperDreamming!!!!!"
#my_long_string = str_pad + my_long_string
#while True:
#    for i in range (0, len(my_long_string)):
#        lcd_text = my_long_string[i:(i+16)]
#        mylcd.lcd_display_string(lcd_text,1)
#        sleep(0.4)
#        mylcd.lcd_display_string(str_pad,1)