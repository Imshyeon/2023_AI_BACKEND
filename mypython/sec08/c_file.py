#seek() 위치를 찾는다
#tell() 현재 파일
def case01():
    # test.txt 파일을 읽어서 seek()를 이용해서 efg를 읽어오자
    with open('test.txt', 'r') as f:
        f.seek(4)
        data = f.read(3)
        pos = f.tell()  #7
        print(data)
        f.seek(0)#처음으로 보낸다.
        data02 = f.read(7)
        pos02=f.tell()
        print(data02)
    print(pos,pos02)


def case02():
    # 데이터를 파일에서 읽어서 tell()을 사용해서 한줄씩 처리 후 번호를 출력해보자
    with open('test.txt', 'r') as f:
        line_number = 1
        f_num=f.tell()
        for line in f:
            print(f'line{line_number} : {line.strip()}')    #문자열의 공백제거
            line_number += 1
            # f_num = f.tell()
        # print(f'현재 파일의 위치 : {f_num}')

if __name__ == '__main__':
    case02()
    print()
    case01()
