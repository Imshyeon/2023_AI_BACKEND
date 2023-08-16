#page 139~. for 구문 연습
fruits=['사과', '바나나', '체리', '메론']
for fruit in fruits:
    print(fruit, len(fruits))

#    
numbers=[1,2,3,4,5]
result = 0

for num in numbers: # num = 1, num=2, num=3, num=4, num=5
    result += num   #result = result(0) + num(1)
                    # r= 1+2, r=3+3, r=6+4, r=10+5
else :    
    print('hap = ', result)
    
    
#
print('=======')
for k, fruit in enumerate(fruits, start = 100): #enumerate(iterable, start=0) //  Return an enumerate object.
    print(f"Index: {k}, fruit: {fruit}")    # (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
