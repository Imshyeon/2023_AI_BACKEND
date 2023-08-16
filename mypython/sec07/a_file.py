def myPrn():
    #apple.jpg를 읽어서 res.jpg로 저장해보자
    mypath = "C:\\pywork\\mypython\\sec07"
    with open(f'{mypath}\\apple.jpg','rb') as f:
        result = f.read()
    with open(f'{mypath}\\res02.jpg','wb') as f:
        f.write(result)

def myread():
    with open('apple.jpg','rb') as file:
        image_data = file.read()
    return image_data
def mywrite():
    image_data = myread()
    with open('res02.jpg','wb') as file:
        file.write(image_data)

if __name__ == '__main__':
    myread()
    mywrite()
    myPrn()
