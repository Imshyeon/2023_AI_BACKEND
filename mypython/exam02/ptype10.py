# -*- coding:utf-8 -*-
#멀티 라인은 반드시 트리쿼터(',")를 사용한다 '''
lines = '''AAA
BBB
CCC'''
print (type(lines)) 

# 문자열을 라인 단위로 분리한 각 원소들을 지닌 리스트 반환
lines2 = lines.splitlines() # Return a list of the lines in the string, breaking at line boundaries
print (type(lines2))

print (lines2)

