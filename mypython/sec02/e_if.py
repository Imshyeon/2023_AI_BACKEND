#page 136. if_test
def if_value(value):
    if value == 1:
        print('value 1')
    elif value == 2:
        print('value 2')
    elif value == 3:
        print('value 3')
    else:
        print('other value')
    
    
def if_value02(value):  #if를 선택문으로 변환 -> get메소드를 주면 dict로 진행
    res={
    1 : 'value 1',
    2 : 'value 2',
    3 : 'value 3'
    }
    print(type(res))
    r=res.get(value,'other value') #help(dict.get) => get(self, key, default=None, /) 
                                   # => Return the value for key if key is in the dictionary, else default.
    print(type(r))  # key에 대한 value 값은 str이니까
    print(r)
              
value=2
if_value(value)
if_value02(value)


#page 137.
def exam(value):
    print(type(value)) # str
    value=value.strip() #공백을 제거해줌
    menu = {
        'spam' : 500,
        'ham' : 700,
        'egg' : 300,
        'spagetti' : 900
    }
    return menu.get(value,0)
    
order='ham '
price=exam(order)
print(price)