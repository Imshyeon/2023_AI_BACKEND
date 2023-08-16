#객체를 활용한 카피
'''
1) copy() 함수 또는 [:'] 를 사용한 shallow copy -> 참조형 (공유, 메모리가 새로 생성되진 않음)
    : 중첩된 객체를 한쪽에서 수정하면 같은 객체를 참조하기 때문에 결과는 동일하다.

2) deepcopy() -> 독립적인 복사본
    : 중첩된 객체를 한쪽에서 수정하면 다른 객체를 참조하기 때문에 결과는 각 개체간 다르다.
'''

import copy

o_list = [1, [2,3], [4,5]]

shallow_copy = o_list.copy()
print(shallow_copy)
#수정
shallow_copy[1][0]=100
print(o_list)   # [1, [100, 3], [4, 5]]


deep_copy = copy.deepcopy(o_list)
deep_copy[1][1] = 30000
print(o_list)   # [1, [100, 3], [4, 5]]
print(deep_copy)    # [1, [100, 30000], [4, 5]]