import requests


# 공공데이터포털 -> "질병관리청_코로나19 국내발생현황 조회" 검색 -> 오픈 api 첫번째 항목 -> 활용신청
# 일반 인증키 (encoding decoding 상관없음)
service_key = 'hQcIj%2FsNvr5evbAwZdltCH7QVzQCMIgotkxaPPQ%2BhJfb6JMUxs7vV7CN9xv4gRCpyCpe%2Fd6pswqVrzmMnEiZZQ%3D%3D'
# 요청주소 + 필수항목으로 신청
url = f'http://apis.data.go.kr/1790387/covid19CurrentStatusKorea/covid19CurrentStatusKoreaJason?ServiceKey={service_key}'

resp = requests.get(url)
# print(resp.text)
# print(resp.json())
# print(type(resp.json()))
print(resp.content)
result=resp.json()['response']['result'][0]
print(f"일일확진 : {result['cnt_confirmations']}")
print(f"일일 신규입원 : {result['cnt_hospitalizations']}")
print(f"일일 사망 : {result['cnt_deaths']}")
# result = resp.json()['response']['result'][0]
# print(result)
# print(f'일일확진 : {result["cnt_confirmations"]}')
# print(f'일일사망 : {result["cnt_deaths"]}')
