# -*- coding:utf-8 -*-
#리턴되는 값들 잘 생각해서 공부하기. ex) 리스트, 문자열..
u = '바나나 포도 수박'
t = u.split()   # 문자열 내의 단어 리스트 , 공백으로 구분
print(type(t))
print( t)

t2 = ':'.join(t)  # 리스트 t 내부의 각 원소들을 ':'로 연결한 문자열 반환
print (type(t2))
print (t2)

