import smtplib
from email.mime.text import MIMEText

def send_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    s.login('보내는메일', '지메일 앱 비밀번호')

    msg = MIMEText('[미세먼지 정보]' +\
                         "\n\n    미세먼지 등급 : " + (message['pm10_data']['grade']) + \
                         "\n    미세먼지 농도 : " + (message['pm10_data']['value']) + \
                         "\n\n    초미세먼지 등급 : " + (message['pm25_data']['grade']) + \
                         "\n    초미세먼지 농도 : " + (message['pm25_data']['value']) + \
                         "\n\n    일산화탄소 등급 : " + (message['co_data']['grade']) + \
                         "\n    일산화탄소 등급 : " + (message['co_data']['value']) + \
                         "\n\n    오존 등급 : " + (message['o3_data']['grade']) + \
                         "\n    오존 등급 : " + (message['o3_data']['value'])
                             )
    msg['Subject'] = '미세먼지 주의 메일'

    s.sendmail("보내는메일", "받는메일", msg.as_string())

    s.quit()