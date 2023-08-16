#정밀도와 반올림을 제어하여 정확한 십진수 산술을 수행
from decimal import Decimal, ROUND_HALF_UP  #선택적으로 import
import math
import f_fileof

#quantize(self, /, exp, rounding=None, context=None)   //self랑 /는 무시..

number = Decimal(math.pi)
decimal_places = 2

rounded_number = number.quantize(Decimal('0.{}'.format('0'*decimal_places)))
rounded_number = rounded_number.quantize(Decimal('0.{}'.format('0'*decimal_places)), rounding=ROUND_HALF_UP)
 
print(rounded_number)

#print(dir(f_fileof))
#print(help(f_fileof.my_file))
#print(help(f_fileof.my_read))
#print(help(f_fileof.my_write))

mystr = \
'''
'ROUND_05UP' : 반올림할 숫자가 소숫점 바로 앞 숫자. 0,5,6,7,8,9 => 5로 올림. // 나머지 숫자는 내림
'ROUND_CEILING': 항상 올림// +방향으로 올림,
'ROUND_DOWN' : 항상 내림// -방향으로 올림,
'ROUND_FLOOR',
'ROUND_HALF_DOWN' : 가장 가까운 방향으로 반올림,
'ROUND_HALF_EVEN',
'ROUND_HALF_UP',
'ROUND_UP' : 항상 올림,
'''

m_file = f_fileof.my_file   # my_file='abc.txt' (in f_fileof.py) 
f_fileof.my_write(m_file)
f_fileof.my_read(m_file)

print(mystr, file=open(m_file, 'w'))
f_fileof.my_read(m_file)