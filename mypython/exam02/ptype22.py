# ‐*‐ coding:utf‐8 ‐*
y_value = [10, 20, 30, 40, 50] 
# 새로운 리스트([60, 70]를 기존 리스트 s_value  뒤에 병합
# extend(iterable, /) // Extend list by appending elements from the iterable.
y_value.extend([60, 70]) 
print ("extend : ", y_value)  #병합한 결과

# 주의: append로 새로운 리스트를 추가하면 하나의 리스트 요소로서 추가 
# append(object, /)
# help ; Append object to the end of the list.
y_value.append([60, 70]) 
print ("append : ", y_value)#추가된 결과

#다른 타입을 원하는 위치에 삽입 
# insert(index, object, /)
# help ; Insert object before index.
y_value.insert(2, ( 'a' , 'b' ))
print ("insert : ", y_value)

