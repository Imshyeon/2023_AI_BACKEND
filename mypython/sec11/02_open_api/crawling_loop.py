from bs4 import BeautifulSoup
import requests


# 공공데이터포털 -> (테마별 - 카테고리별) 교육 -> 파일데이터
url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
paging = soup.find('nav', {'class': 'pagination'})


nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, paging)))
print(nums)
for i in nums:
    sub_url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=' + i
    soup = BeautifulSoup(requests.get(sub_url).text, 'html.parser')
    # titles = soup.find_all('span', class_='title')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())
