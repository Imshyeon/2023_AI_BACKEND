import math     #수학 함수 (일반 숫자)
import cmath    #켤레 복소수연산 함수 모듈 (복소수 전용)

#모듈을 사용하지 않고 부동소수점 자리 변경을 하는 방법
#print = format 1) "format"%(value)     2)"객체".format(value,,,,(자리수))      3)f""
#1. 문자열 사용 방법 = 출력 서식으로    %c : 한문자, %s: string, %d: 10진, %o: 8진, %x: 16진, %f: 부동소수
                                     # %5.1f-> %전체자리수.소수이하자리수f            
number  = math.pi 
decimal_places =2
formatter_number = "{:.{}f}".format(number, decimal_places) #str.format
print(formatter_number)

#2. round() 이용 = 수치값 변경
#number=3.141592
number=math.pi
decimal_places = 2
round_number = round(number, decimal_places)    
print(round_number)     #3.14
print(math.pi, cmath.pi)    #3.141592653589793 3.141592653589793