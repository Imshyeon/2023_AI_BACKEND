from bs4 import BeautifulSoup
import urllib.request


# naver -> 영화 -> 상영작 예정작
resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver')
soup = BeautifulSoup(resp, 'html.parser')

movies = soup.find_all('dl', class_='lst_dsc')

for movie in movies:
    title = movie.find('a').get_text()
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))
