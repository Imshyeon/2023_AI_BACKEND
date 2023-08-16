#page 36. 표준 입출력 정보

import sys # 시스템의 작동방식 등 정보[path, version 등] 모듈, 단 시스템설정, 동작방식 변경 제공하지 않음.
           # sys -> float_info -> [10/3] -> decimal 모듈 -> decimal.getcontext()을 봐야함
#float 정보 => 부동소수점 조작, 제어 = decimal 라이브러리, numpy라이브러리(배열)
print(f"Epsilon : {sys.float_info.epsilon}")    #f : print format => {}안의 변수를 호출 가능
print(f"Digits : {sys.float_info.dig}") #10진수는 자리 여기까지.. 라는 의미
print(f"Maximum : {sys.float_info.max}")
print(f"Minimum : {sys.float_info.min}")
print(f"Minimum base-10 : {sys.float_info.min_10_exp}") 
print(f"Maximum base-10: {sys.float_info.max_10_exp}")  #최대 지수

print(f"Minimum base : {sys.float_info.min_exp}") 
print(f"Maximum base : {sys.float_info.max_exp}")