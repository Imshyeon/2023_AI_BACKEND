#apple.jgp를 읽어서 다른이름으로 저장
import shutil
#from  PIL import Image
import imageio
import imageio.v3 as iio
def case01():
    #1. stream 단위로 파일을 저장 (for binary files)
    with open("apple.jpg" ,"rb") as f1:
        with open("apple_copy.jpg" ,"wb") as  f2:
            f2.write(f1.read())
def case02():
    # 2.shutil  단위로 파일을 저장 (for binary files)
    shutil.copyfile("apple.jpg" ,  "apple_copy02.jpg")
def case03():
    # 3.PIL를 이용한  파일 저장  ( Python Imaging Library)
    # image   = Image.open("apple.jpg")
    # image.save("apple_copy03.jpg")
    pass

def case04():
    #4.imageio를 사용하는 방법
    img  = iio.imread("apple.jpg")
    iio.imwrite("apple_copy04.jpg", img)

if __name__ == '__main__':
    case04()