from selenium import webdriver #브라우저를 실행할 수 있는 드라이버 자체적으로 실행. 변동되는 화면들을 찾아옴
                               #chrome으로 찾아온다.
from bs4 import BeautifulSoup
from time import sleep


url = 'https://comic.naver.com/webtoon?tab=tue'
#드라이버를 실행하겠다
service = webdriver.chrome.service.Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

sleep(3)
driver.get(url) #브라우저 실행해서 url 요청을 한다.

sleep(10)   #sleep이 있어야 긁어올 수 있음.
soup = BeautifulSoup(driver.page_source, 'html.parser') #파싱
# print(soup)

li_list = soup.select('.component_wrap .item')
print(li_list)

for li in li_list:
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    #<span class = "ContentTitle__title--e3qXt"> -> <span class="text"> 김부장</span> ..
    #그래서 끝의 .text는 class 명이다. 그래야지 안의 text를 받아올 수 있음
    star = li.find('span', class_='Rating__star_area--dFzsb').text
    print(f'{star} "{title}"')

driver.close()


'''
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

url="https://comic.naver.com/webtoon?tab=tue"
service = webdriver.chrome.service.Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

sleep(3)
driver.get(url)

sleep(10)
soup=BeautifulSoup(driver.page_source,'html.parser')
#<div class="TripleRecommendList__info_area--DVTdh"><a class="ContentTitle__title_area--x24vt" href="/webtoon/list?titleId=711422"><span class="ContentTitle__title--e3qXt"><span class="text">삼국지톡</span></span></a><div class="ContentAuthor__author_wrap--fV7Lo"><a class="ContentAuthor__author--CTAAP" href="/webtoon">무적핑크 / 이리</a><div tabindex="0" style="outline: 0px;"></div></div><p class="TripleRecommendList__sub_title--LFalt"><a href="/webtoon/detail?titleId=711422&amp;no=503&amp;week=tue">한중왕,유비_24.엎친데 덮친데 겹친 조조</a></p><div class="rating_area"><span class="Rating__star_area--dFzsb"><i class="Rating__ico_star--BcfMb"><svg width="12" height="19" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.25 12.991a.529.529 0 0 0-.5 0l-2.578 1.384a.529.529 0 0 1-.753-.632l.882-2.682a.529.529 0 0 0-.17-.576L.596 8.438a.529.529 0 0 1 .299-.94l3.049-.191a.529.529 0 0 0 .457-.33L5.51 4.22a.529.529 0 0 1 .982 0l1.107 2.756c.077.19.255.318.458.33l3.049.192c.481.03.674.637.299.94l-2.535 2.047a.529.529 0 0 0-.17.576l.881 2.682a.529.529 0 0 1-.752.632L6.25 12.99Z" fill="#999"></path></svg><span class="blind">별점</span></i><span class="text">7.83</span></span></div></div>
li_list=soup.select('div.component_wrap .TripleRecommendList__info_area--DVTdh')
print(li_list)

for li in li_list:
    title = li.select('a')[0].get_text()
    star = li.select('div.rating_area .text')[0].get_text()
    print(f'{title}\t{star}')

driver.close()
'''