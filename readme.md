## 미세먼지측정 데이터를 이용한 LED Indicator 제작

### 에어코리아 API를 이용하여 실시간 미세먼지 데이터 받아오기
#### 에어코리아 API 이용 방법.

* `공공데이터포털 회원가입` - [링크](https://www.data.go.kr/index.do, "공공데이터 포털")
* `미세먼지 대기오염정보 검색` 

![search](/images/search.png)

* `한국환경공단_에어코리아_대기오염정보` - 오픈API - 한국환경공단_에어코리아_대기오염정보

![search](/images/search2.png)

* `활용 신청` - 주어진 폼 작성

![get_api](/images/get_api.png)

* `마이페이지-오픈API-개발계정-한국환경공단_에어코리아_대기오염정보`

![get_api](/images/get_api2.png)

* `API_KEY` - API_KEY 확인
* `상세 설명`

![API](/images/api_key.png)

* `목록 - 원하는 목록 선택` - 요청 주소 확인

![URL](/images/url.png)

#### API_KEY + Request

1. import module
```python
import json
import requests
```
2. API_KEY
```python
API_KEY = "발급받은 API_KEY"
```
3. Request URL
```python
# 시-도별 조회 요청 URL
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
```
4. Parsing
```python
res = requests.get(url, params).text
data = json.loads(res)
```
5. Finish



