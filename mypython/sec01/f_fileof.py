#page 39. 1) 파일 입출력 함수를 만들어서 호출하고 
#2) print()를 이용해서 파일 입출력, 
#3) 현재 모듈 f_fileof.py를 e_decimalof.py로 import 시켜서 
#4) 문자열을 print 함수로 출력하고 file의 결과를 확인
#5) 사용자가 파일이름, 쓰고싶은 자료를 넘겨서 저장하는 코드
#6) 모듈의 함수에 선언된 doc string을 지정해서 help로 확인.


#abc.txt 파일에 my_write(), my_read() 두개의 함수를 통해서 파일 입출력
def my_write(my_file):
    """ 파일을 쓴다. my_file = '파일의 이름' """
    f=open(my_file,'w')
    f.write('11111111\n')
    f.write('22222222\n')
    f.close()

def my_read(my_file):
    """ 파일을 읽는다 """
    f=open(my_file,'r')
    print(f.readlines())
    f.close()
    
my_file='abc.txt'    
# my_write(my_file)
# my_read(my_file)


# print(1,2,3,4,5,6,7, file=open(my_file,'w'))
# my_read(my_file)

#page 39
#사용자가 파일이름, 쓰고싶은 자료를 넘겨서 저장하는 코드
def my_write02(my_file,my_data):
    """
    파일을 쓴다.
    my_file = '파일의 이름'
    my_data = '쓸 문장'
    """
    
    f=open(my_file,'a')
    f.write(my_data+'\n')
    f.close()

# my_write02(my_file,'abcdefg')
# my_read(my_file)

'''
1. f.read()
11111111
22222222
~blurblurblur~
'''

'''
2. f.readline()
11111111
'''

'''
3. f.readlines()
['11111111\n', '22222222\n', '~blurblurblur~']
'''

'''
4. f.readable()
True
'''