import smtplib, os, pickle
from email import encoders
from email.mime.text import MIMEText as text
from email.mime.multipart import MIMEMultipart as send_email
from email.mime.base import MIMEBase

# address = ["y2kdj9723@naver.com"]
# pw = "123"

# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()
# smtp.login('y2kdj9723@naver.com', "123")

# msg = send_email()
# msg['Subject'] = '미세먼지 주의 메일'

# part = text('미세먼지 등급이 매우 나쁨입니다')
# msg.attach(part)

# msg["To"] = address
# smtp.sendmail('y2kdj9723@naver.com', address, msg.as_string())

import datetime
import time

while True:
    now = datetime.datetime.now()
    minute = str(now.minute)
    second = str(now.second)
    
    if (second == "30"):
        print(minute, "분", second, "초")
        time.sleep(1)