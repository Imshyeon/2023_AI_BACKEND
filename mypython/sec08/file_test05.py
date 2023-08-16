#피클링 작업을 해보자  byte, char, object(시퀀스나 클래스)
#직렬화(pickle) : 바이트 스트림으로 변환, 역직렬화(unpickle) : 바이트 스트림에서 객체로 변환
#확장자 : .pkl(피클링한 파일)
try:
    import cPickle  # 임포트 cPickle   -> 객체를 피클링하는 모듈/ dump(), load()
    pickle = cPickle #pickle로 대입한다, 대입시 cPickle이 없다면 프로그램은 중단이 되기 때문에 except로 이동
except:
    import pickle  #임포트 pickle

book ={'java':30000,'jsp':35000,'oracle':40000, 'python': 20000}
list =["abcd",90,90.8]
Tuple =(book, list)
print(Tuple)

f= open('ptest.txt','wb' )
pickle.dump(Tuple,f) #파일에 객체를 저장
f.close()

f = open("ptest.txt","rb")
res01, res02= pickle.load(f)    #load : 객체 단위로 분할 잘 해줌..
print("res01(book)-->",res01)
print("res02(list)-->",res02)

