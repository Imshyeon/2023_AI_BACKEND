#test_file03 -> with문으로 수정한 클래스
class MyFIle:
    def __init__(self,mypath,mystr ):
        self.mypath = mypath
        self.mystr = mystr

    def My_write(self):
        with open(self.mypath,'a') as f:
            f.write(self.mystr)

    def My_read(self):
        with open(self.mypath,'r') as f:
            print(f.read())

if __name__ == '__main__':
    # mypath = "c:\\test\\data.txt" # test_file06
    mypath = "data_test.txt"    #b_file
    my_dict="{1:'a',2:'b',3:'c'}"
    # m1 = MyFIle(mypath, "abcdefg") #생성자 호출 - test_file06
    m1 = MyFIle(mypath, my_dict)    #b_file
    m1.My_write()
    m1.My_read()

