import json
import requests

API_KEY = "발급받은 API_KEY"

# url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth" # 대기질 예보통보 조회
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty' # 시-도 별 조회
params = {
    'serviceKey' : API_KEY,
    'serviceKey' : '발급받은 API_KEY', 
    'returnType' : 'json',
    'numOfRows' : '100',
    'pageNo' : '1',
    'sidoName': '경기',
    'ver': '1.0'
    }

res = requests.get(url, params).text
data = json.loads(res)

air_pollution_data = data['response']['body']['items']

print(air_pollution_data)

for i in range(len(air_pollution_data)):
    print(i, air_pollution_data[i]["stationName"])
    if air_pollution_data[i]['stationName'] == "고색동" :
        in_kosaek_air = air_pollution_data[i]        
    elif air_pollution_data[i]['stationName'] == "인계동":
        in_ingye_air = air_pollution_data[i]
        
# in_kosaek_air = air_pollution_data[6] # 고색동
# in_ingye_air = air_pollution_data[6] # 인계동

PM10_value1 = in_kosaek_air['pm10Value']
PM10_grade1 = in_kosaek_air['pm10Grade']
PM25_value1 = in_kosaek_air['pm25Value']
PM25_grade1 = in_kosaek_air['pm25Grade']
print(in_kosaek_air)

PM10_value2 = in_ingye_air['pm10Value']
PM10_grade2 = in_ingye_air['pm10Grade']
PM25_value2 = in_ingye_air['pm25Value']
PM25_grade2 = in_ingye_air['pm25Grade']
print(in_ingye_air)

# PM10: 미세먼지 등급 기준(국내)
# 좋음: 0~30
# 보통: 31~80
# 나쁨: 81~150
# 매우나쁨: 151~

#PM25: 초미세먼지 등급 기준(국내)
# 좋음: 0~15
# 보통: 16~35
# 나쁨: 36~75
# 매우나쁨: 76~



print(PM10_value1, PM10_grade1, PM25_value1, PM25_grade1)
print(PM10_value2, PM10_grade2, PM25_value2, PM25_grade2)