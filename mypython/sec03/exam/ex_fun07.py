# 커피 자판기 프로그램

# >> 결과화면 <<
# ===== 메뉴 =====
# 1. 아메리카노
# 2. 카페라떼
# 3. 카푸치노
# 4. 종료
# ================
# 메뉴 선택: 1
# 아메리카노를 선택하셨습니다.

###기능1 : 현재 금액 출력
money = int(input('돈 입력: '))
print('★ 현재 %d원 있습니다. ★\n' % money)

###기능2: 메뉴 출력
print('======== 메뉴 ========')
print('1. 아메리카노(1000원)')
print('2. 카페라떼(1500원)')
print('3. 카푸치노(2000원)')
print('4. 종료')
print('======================')

###기능3. 선택한 메뉴를 현재 금액에 따라 구매 유무
n = int(input('메뉴 선택: '))

if n == 1:
    if money < 1000:
        print('돈이 부족합니다.')
    else:
        money = money - 1000  # money -= 1000
        print('아메리카노를 구매하셨습니다.')

    print('★ 현재 %d원 있습니다. ★\n' % money)

elif n == 2:
    if money < 1500:
        print('돈이 부족합니다.')
    else:
        money = money - 1500  # money -= 1500
        print('카페라떼를 구매하셨습니다.')

    print('★ 현재 %d원 있습니다. ★\n' % money)

elif n == 3:
    if money < 2000:
        print('돈이 부족합니다.')
    else:
        money = money - 2000  # money -= 2000
        print('카푸치노를 구매하셨습니다.')

    print('★ 현재 %d원 있습니다. ★\n' % money)

elif n == 4:
    print('종료합니다.')

else:
    print('1~4 사이만 입력 가능합니다.')

