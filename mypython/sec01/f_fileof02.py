###########     open() 객체와 with ~ as문 
#with를 사용하면 close를 사용하지 않아도 된다.

def my_write(my_file):
    """ 파일을 쓴다. my_file = '파일의 이름' """
    with open(my_file,'w') as f:
        f.write('11111111\n')
        f.write('22222222\n')
        #자동 close() :  내부적으로 close를 호출.

def my_read(my_file):
    """ 파일을 읽는다 """
    with open(my_file,'r') as f:
        print(f.readlines())

my_file= 'f02.txt'

#사용자가 파일이름, 쓰고싶은 자료를 넘겨서 저장하는 코드
def my_write02(my_file,my_data):
    """ 
    파일을 쓴다. 
    my_file = '파일의 이름'
    my_data = '쓸 문장' 
    """
    with open(my_file,'a') as f:
        f.write(my_data+'\n')

my_write02(my_file,'123456')
my_read(my_file)