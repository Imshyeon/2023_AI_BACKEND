import http.client

from bs4 import BeautifulSoup
import urllib.request

def Test04():
    #HTTPConnection 객체로 접속 : 값을 줄수도 있고 받을 수 있다.
    conn = http.client.HTTPConnection('www.myserver.org')
    conn.request('GET','/')
    res=conn.getresponse()
    print(res.msg,type(res.msg))
    for key, value in res.msg.items():
        print(key ,"===>", value)
    print('\nkeys()')
    for key in res.msg.keys():
        print(key)
    print('\nvalues()')
    for value in res.msg.values():

        print(value)

def Test():
    #파이선 페이지 글을 300자만 출력 // urlopen은 get만.. 그니까 받아오는 것만 가능
    f=urllib.request.urlopen("https://www.python.org/") #페이지요청을 바로해서 다운로드
    print(f.read(300).decode('utf-8'))

def Test01():
    #파이선 페이지 글을 300자만 출력
    req=urllib.request.Request('https://www.myserver.org/')#서버에 요청을 한다.
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print("--------->",e.reason)

def Test02():
    #파이선 페이지 글을 300자만 출력
    req=urllib.request.Request('https://www.myserver.org/')#서버에 요청을 한다.
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as h:
        print("1",h.code)  #503(400대는 서버는 돌아가지만 요청한 값이 없거나 권한이 없거나..)
        #오류메시지
        print("2",h.msg)  #Service Unavailable
        #http응답과 관련된 헤더 오류 - hdrs
        #요청을 받았을 때 브라우저의 헤더값들..
        print("3",h.hdrs)   #Content-Type: text/html; charset=us-ascii
                            # Server: Microsoft-HTTPAPI/2.0
                            # Date: Thu, 20 Jul 2023 07:28:22 GMT
                            # Connection: close
                            # Content-Length: 326

        #파일
        print("4",h.fp) #<http.client.HTTPResponse object at 0x000001FF224BA770>
        print("5",h.url)    #https://www.myserver.org/
        print("6",h)    #__repr__ : HTTP Error 503: Service Unavailable

def Test03():
    #파이선 페이지 글을 300자만 출력
    response=urllib.request.urlopen("https://www.python.org/doc/") #페이지요청을 바로해서 다운로드
    print("1. response: ",response)    #HTTPResponse
    print("2. URL:", response.geturl())    #URL: https://www.python.org/doc/
    print("3. info:",response.info(),type(response.info()))
    hearders=response.info()
    print("4. ",hearders['date'])

if __name__ == '__main__':
    Test03()