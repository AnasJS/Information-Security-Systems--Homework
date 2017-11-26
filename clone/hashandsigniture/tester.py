# n = bytes(b'45')
#
# print(n.decode('utf-8'))
# dic = {1:5 ,5:4}
# print(dic[5])
# print(bytes([1]))
#
# s = bytearray([1])
# s+= bytearray([2])
# s+= bytearray([3])
# s+= bytearray([4])
#
# #
# # print(type(s))
# print(s[0:1])
from rc4 import *
data = bytearray([55])
print(data.decode('utf-8'))
print(type(data.decode()))
c= encrypt(data.decode('utf-8'),data.decode('utf-8'))
print("data encrypted {c}".format(c = c))
print(c)
# e=''.join(chr(x) for x in c)
# ee=bytearray(e)
# print(e)
r  =decrypt( data, data.decode('utf-8'))
# print("data ddecrypted {r}".format(r=r))
anas = "anuas"
print(anas[:-2])
print(anas[-2:])
