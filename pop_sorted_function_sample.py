#!/usr/bin/env python

#通过基础应用说明sorted()函数是用来排序的

numbers = [1,2,-3,-4]
print(sorted(numbers))

#sorted()函数还可以通过key接收一个自定义排序方法

print(sorted(numbers,key = abs))

#sorted()还支持字符串排序，字符串排序是根据ASCII码大小排列的

strs = ['messi','Xavi','Iniesta']
print(sorted(strs))

#可以使用lower或capitalize方法来实现忽略首字母大小写排序

print(sorted(strs,key = str.capitalize))
