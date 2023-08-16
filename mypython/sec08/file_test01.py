#2진화 코드분                byte, char, object(node) (=> stream으로 관리)로 파일 입출력
#                           직렬화, 역직렬화를 해줌.
#                           byte, char -> open // object -> 피클(직렬화), 인피클(역직렬화)
class BTest:
    def b_wrtie(self):
        f = open("file_test01.txt",'wb')
        f.write(b'ABC1234') # 1byte 이내 코드값 변환   ASCII   ,  (확장형 코드 =  scan code(function, 방향키) , unicode 2byte = 0~65535)
        f.close()
    #키보드 버퍼 -> [버퍼링] stream(IO 작업) -> 파일
    def b_read(self):
        f= open("file_test01.txt","rb")
        while   True:
            s = f.read(1)   #한 글자씩 뽑아서 s에 넣겠다.
            if s ==b'':     #EOF
                break
            print(s.hex(), s)
        f.close()

if __name__ == '__main__':
    b1= BTest()  #기본 생성자를 호출하면서 객체를 생성한다.  __init__(self)
    b1.b_wrtie()
    b1.b_read()
