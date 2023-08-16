from bs4 import BeautifulSoup   #html, xml, xpath, lxml을 파싱하는 모듈
import urllib.request #웹페이지 다운로드 받는 모듈
from selenium.webdriver import Keys #드라이버를 통해서 실행된 브라우저를 제어하는 키 값
from selenium import webdriver #드라이버를 통해 브라우저를 실행시킨다.
import time #중간 중간에 sleep을 걸자.

def fetch_images():
    #1. 드라이버를 통해 브라우저를 인스턴스화
    service = webdriver.chrome.service.Service('C:/')
    browser = webdriver.Chrome(service=service)

    #2. 검색창에 가서 원하는 이미지를 로드해보자.
    browser.get('https://www.google.com/imghp?hl=ko&ogbl')

    #xpath : //*[@id="APjFqb"]
    #요소 : <textarea class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1" aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false" aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="검색" type="search" value="" aria-label="검색" data-ved="0ahUKEwiRut6tnb2AAxVINt4KHZHsAtwQ39UDCAM"></textarea>
    #selector : #APjFqb

    #3. 검색어 입력 상자를 찾아온다.
    elem=browser.find_element("xpath", '//*[@name="q"]')
    #4. 검색어를 입력한다.
    elem.send_keys("사과") #스크롤링 하고 싶은 검색어
    #5.엔터를 누른다.
    elem.submit()   #서버에 요청

    #6. 2번 스크롤 내려가는 상태
    for i in range(1,2):
        browser.find_element("xpath", '//body').send_keys(Keys.ENTER)
        time.sleep(10)  #End키를 누르고 내려가는 시간이 걸려서 sleep을 해줌
    time.sleep(10) #네트워크 상태 느릴까봐 안정성을 위해 sleep()을 해준다.
    html = browser.page_source  #브라우저의 소스코드를 다운로드 받는다.
    soup=BeautifulSoup(html,'lxml')
    # print(soup)   #전쳋 다운로드 한 문서의 내용확인

    #7. 그림 파일을 저장하자. class="rg_i Q4LuWd" 구글의 이미지 태그
    imgList = soup.find_all("img", class_="rg_i Q4LuWd")   #파싱하고
    params = []
    for img in imgList:
        try:
            params.append(img["src"])
        except KeyError:
            params.append(img["data-src"])

    #8. 원하는 폴더에 이미지를 저장하자.
    # import urllib.request.urlretrieve('http://www.exam.com/test/a.zip' , 'c:\test\y.zip')
    for idx, p in enumerate(params,1):
        # img_folder = "c:/img/" 관리자권한으로 만들어져야하는 폴더일때 안됨.. 다시한번 볼 필요가 있다.
        urllib.request.urlretrieve(p, "C:/pywork/img/" + str(idx)+ "_google.jpg")

def test():
    #C:\pywork\mypython\sec11\01_naver
    service = webdriver.chrome.service.Service('C:/')
    driver = webdriver.Chrome(service=service)  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/');
    time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')   #검색창
    search_box.send_keys('ChromeDriver')    #검색키워드
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()

if __name__ == '__main__':
    fetch_images()
