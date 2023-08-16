#모듈을 임포트해서 호출만 해보자
import f_fileof

print('파일을 확인 : ',f_fileof.my_file)
g_file=f_fileof.my_file
f_fileof.my_write(g_file)
f_fileof.my_read(g_file)


print('heeelllooo',file=open(g_file,'a'))
f_fileof.my_read(g_file)

############### 파일 이름, 데이터를 넘겨서 파일 관리
#page 39

#print(help(f_fileof.my_write02))
f_fileof.my_write02("g_ex.txt","abcdefg")
f_fileof.my_read("g_ex.txt")