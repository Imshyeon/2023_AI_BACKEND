import requests
from xml.etree import ElementTree


# 공공데이터포털 -> "보건복지부_코로나19 확진자 성별 연령별 현황" 검색 -> 오픈 api 첫번째 항목 -> 활용신청
# 일반 인증키 (encoding decoding 상관없음)
service_key ='hQcIj%2FsNvr5evbAwZdltCH7QVzQCMIgotkxaPPQ%2BhJfb6JMUxs7vV7CN9xv4gRCpyCpe%2Fd6pswqVrzmMnEiZZQ%3D%3D'
# 요청주소 + 필수항목으로 신청
url = f'http://apis.data.go.kr/1352000/ODMS_COVID_05/callCovid05Api'
query_string_key = f'serviceKey={service_key}'
query_string_page = f'pageNo={1}'
query_string_rows = f'numOfRows={9999}'

url_with_querys = url + f"?{query_string_key}&{query_string_page}&{query_string_rows}"
# print(url_with_querys)

resp = requests.get(url_with_querys)
tree = ElementTree.fromstring(resp.text)
print(tree)
print(tree[0])
print(resp.content)

for item in tree[1][0]:
    print(item)
    if item.find('createDt').text.split('-')[0] == "2023":
        createDt = item.find('createDt').text
        gubun = item.find('gubun').text
        confCase = item.find('confCase').text
        death = item.find('death').text
        message = f'등록일: {createDt}\n연령: {gubun}\n확진자수: {confCase}\n사망자수: {death}\n'
        print(message)
