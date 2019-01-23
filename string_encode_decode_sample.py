#!/usr/bin/env python

#python3字符串为Unicode编码，可以直接在内存中使用，但是如果字符串用来存储或传输时，需要将字符串转换为字节为单位的bytes

#encode()：从Unicode转为bytes，decode()：从bytes转为Unicode

#type()查看数据类型

str = 'IoT'
print(str)
print(type(str))
print(str.encode())
print(type(str.encode()))

x = b'IoT'
print(x)
print(type(x))
print(x.decode())
print(type(x.decode()))
