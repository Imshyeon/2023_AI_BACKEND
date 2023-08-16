from dataclasses import make_dataclass
# #test_file03 ->python모듈을 사용해서 변환
MyFile = make_dataclass(
    "MyFile",
    fields=[("mypath", str), ("mystr", str)],
    namespace={
        "my_write": lambda self: self._write_file(self),
        "my_read": lambda self: self._read_file(self),
        "_write_file": lambda self: self.__class__._write_file(self),
        "_read_file": lambda self: self.__class__._read_file(self),
    },
)
#namespace에서 위임받아서 여기서 씀.
@staticmethod   #단독객체를 접근하는 거기 때문에? staticmethod
def _write_file(self):#self가 있어야 클래스의 멤버라는 걸 안다.
    with open(self.mypath,'a') as f:
        f.write(self.mystr)

@staticmethod
def _read_file(self):
    with open(self.mypath, 'r') as f:
        print(f.read())

MyFile._write_file = _write_file
MyFile._read_file = _read_file

if __name__ == '__main__':
    my_file=MyFile("file.txt","Hello,World!")
    my_file.my_write()
    my_file.my_read()