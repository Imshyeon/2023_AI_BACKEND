from bs4 import BeautifulSoup
import requests

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EC%BD%94%EB%A1%9C%EB%82%9819&operator=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=_score&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
resp=requests.get(url)
soup=BeautifulSoup(resp.text,'html.parser')
paging = soup.find('nav', class_='pagination')
#paging = soup.select('nav.pagination')

nums=list(filter(None,map(lambda x : x.text if x.text.isdigit() else None,paging)))

for i in nums:
    print(f"{i}page======")
    sub_url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EC%BD%94%EB%A1%9C%EB%82%9819&operator=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=_score&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={i}&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
    soup=BeautifulSoup(requests.get(sub_url).text,'html.parser')
    datas = soup.select('div.info-data p:nth-child(2) span.data')
    titles = soup.select('span.title')
    for title,data in zip(titles,datas):
        print(f"{title.text.strip()} :: {data.text.strip()}")


