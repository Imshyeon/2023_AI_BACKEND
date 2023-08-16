# -*- coding:utf-8 -*-
my_list=['cat','rat','dog','money']
print(my_list)

my_list[0]='puppy'     #my_list[0] 번지  값 수정
print(my_list)

del my_list[0]  #객체를 삭제  -> 그 자리에 객체를 생성할 수 있다
print(my_list)

my_list.remove('rat') #요소(인덱스) 삭제 -> 그 자리에 동적할당을 할 수 없다
print(my_list)

my_list.append((10,20,30))#객체를 추가 (tuple)
print(my_list)

my_list.remove((10,20,30)) #값으로 삭제 
#del my_list[2]  #객체를 삭제 
print(my_list)

#clear는 방은 있다.
#remove 방 없다?
#del 은 clear도 없고 remove도 없고 동적할당 가능하도록..