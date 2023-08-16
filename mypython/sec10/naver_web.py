# 네이버 Papago NMT API 예제
import os
import sys
import urllib.request
client_id = "Bae5dMy1zkxmvwAEhIl7"
client_secret = "HjrMt7BCTm"
encText = urllib.parse.quote("안녕하세요 내 이름은 강수현이고, 나중에 런던에서 사는 개발자가 되고싶습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)