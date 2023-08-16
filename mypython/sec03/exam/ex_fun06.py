#page 138
#조건 -> [선택문, 삼항연산자, dict] -> 시퀀스

#1. 삼항연산자 사용
a=10
x = a * 2 if a > 5 else a / 2   #만일에 a>5이면 a*2를 리턴 후 x에 대입하고
print(x)                        # 그렇지 않으면 a/2를 리턴 후 x에 대입
#결과 : 20

#---------------------
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
#---------------------
select=0
if select == 0 :
    result = add(2,3)
else:
    result = sub(2,3)
print(result)   #결과 : 5

#(add,sub)[select](2,3)
#(호출 함수명,,)[비교변수 or 조건식](함수전달 값,,)
#---------------------
a=10
if a>5:
    res=add(3,4)
else:
    res=sub(3,4)
print(res)

#{True:add, False:sub}[a>5](3,4)
#{호출함수명,,}[비교변수 or 조건식](함수전달 값,,)
# dict/tuple       list


#========review===========
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

select=0
print((add,sub)[select](2,3))   #5
#(호출 함수명,,)[비교변수 or 조건식](함수전달 값,,)

a=10
print({True:add, False:sub}[a>5](3,4))  #7
#{호출함수명,,}[비교변수 or 조건식](함수전달 값,,)