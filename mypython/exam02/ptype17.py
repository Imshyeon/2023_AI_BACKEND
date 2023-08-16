# -*- coding:utf-8 -*-
my = (1,'b','c')*3
my = ('a','b','c')*3
print(my)
print( my.index('a'))   # Return first index of value.
print( my.count('a'))   # Return number of occurrences of value.

print(type(my))
print(type(my[0])) #만약 my[0]가 'a'면 type은 str
