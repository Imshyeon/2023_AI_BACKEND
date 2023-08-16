#page 132.
import binascii # 2진 데이터 관리 모듈
print(binascii.hexlify(b'abc'))    #바이트 열 // Hexadecimal representation of binary data.
buf=bytearray(b'abcde')     # bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
print(binascii.hexlify(buf))   #바이트 배열 //
print(binascii.unhexlify(b'6162636465')) #16진 바이트 열 -> 2진 바이트 열