#모듈을 임포트해서 별칭으로 바꾼다음 호출만 해보자
import f_fileof as f

print('파일을 확인 : ',f.my_file)
g_file=f.my_file
f.my_write(g_file)
f.my_read(g_file)

print('heeelllooo',file=open(g_file,'a'))
f.my_read(g_file)

############### 파일 이름, 데이터를 넘겨서 파일 관리
#print(help(f_fileof.my_write02))
f.my_write02("g_ex.txt","abcdefg")
f.my_read("g_ex.txt")