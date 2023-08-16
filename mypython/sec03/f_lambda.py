#---------if문을 사용해서 lambda 연습
def lambda01():
    num=5
    res=lambda x:'positive' if x>0 else 'non-positive'  #x는 매개 변수
    print(res(num))

def lambda02():
    #문자열 길이가 0이면 empty, non-empty
    string=' '
    check_empty = lambda s : 'empty' if len(s)==0  else 'non-empty'
    result= check_empty(string)
    print(result)

def lambda03():
    #입력한숫자가 짝수면 even, odd
    num=7
    check_num = lambda n: 'even' if n%2 == 0 else 'odd'
    result = check_num(num)
    print(result)

def lambda04():
    #입력한 list객체의 요소가 없으면 empty, non-empty
    mylist=[1,2,3]
    check_mylist = lambda l : 'empty' if len(l)==0 else 'non-empty'
    result=check_mylist(mylist)
    print(result)

def lambda05():
    #내가 입력한 숫자가 3의 배수와 5의 배수이며 divisible, not divisible
    num=15
    check_mynum = lambda n :'divisible' if (num%3==0) & (num%5==0) else 'not-divisible'
    result=check_mynum(num)
    print(result)

def lambda06():
    #['a','e','i','p','y','t','h'] 안에 내가 입력한 글자 있으면 yes, no
    li=['a','e','i','p','y','t','h']
    s='H'
    s=s.lower()
    check_mystr = lambda s : 'yes' if s in li else 'no'
    result=check_mystr(s)
    print(result)


if __name__ == '__main__':
    lambda01()  #positive
    lambda02()  #non-empty
    lambda03()  #odd
    lambda04()  #non-empty
    lambda05()  #divisible
    lambda06()  #yes
