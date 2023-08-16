#page 104.
'''
데이터 관리 기분
    1. index : list, tuple, str => 중복 데이터 허용O,  null값 허용
    2. value : set => 중복 데이터 허용X, null값 허용 후 데이터로 처리
    3. key : dict(=map) => key 중복값 허용X, value는 허용 
'''
a={1,2,4,8}
b={5,6,7,8}

#합집합
union = a.union(b) # Return the union of sets as a new set.
print(union)    # a | b
print(a)
print(b)

#교집합
intersection =a.intersection(b) #Return the intersection of two sets as a new set.
print(intersection)     # a & b

#차집합
difference=a.difference(b) # Return the difference of two or more sets as a new set.
print(difference)   # a - b

#배타 = 대칭집합 = 한 집합 또는 다른 집합에서 보유하지만 집합 간에 공유되지 않는 요소.
symmetric_difference=a.symmetric_difference(b) # Return the symmetric difference of two sets as a new set.
print(symmetric_difference)     # a ^ b

sym_d2= a.union(b) - a.intersection(b)
print(sym_d2)

'''
symmetric_difference_update() : 두 개의 set 집합에서 공통 요소 제거 후, 각 고유값을 유지. 
    ex) a. symmetric_difference_update(b)

union() : 중복을 제외한 두 set 집합의 모든 요소를 포함하는 새로운 집합(set)을 만든다.
    ex) union_set = a.union(b)
'''