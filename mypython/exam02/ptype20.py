# -*- coding:utf-8 -*-

mylist=['a','b',[3.58,'d',4,0]]

print('b' in mylist)    # “b”가 mylist에 있는지 유무를 리턴 한다. 
print( 'e' not in mylist ) #“e”가 mylist에 없는지의 유무를 리턴

print('d'  in mylist[2])#“d”가 mylist[2]에 있는지 유무를 리턴 한다. 

######
mylist=['a','e',[3.58,'b',4,0]]
print('b' in mylist)    # “b”가 mylist에 있는지 유무를 리턴 한다. 

mylist=['a','e',[3.58,['b'],'k',0]]
print('b' in mylist[2][1])    # depth까지 적어야지 찾는다..
print('k' in mylist)