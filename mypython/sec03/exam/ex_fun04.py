#page 137.
order = 'spagetti'
if order == 'spam':
    price = 500
elif order == 'ham':
    price = 700
elif order == 'egg':
    price = 300
elif order == 'spagetti':
    price = 900
else:
    price = 0

print(f'{order} 의 가격은 {price} 원 이다 ')

#dict.get(key, default=None, /)
###선택문으로 변형
menu = { 'spam':500, 'ham':700, 'egg':300, 'spagetti':900 }
prce = menu.get( order, 0 ) # 0은 키가 없을 때의 기본값
print(f'{order} 의 가격은 {price} 원 이다 ')