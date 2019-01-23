#!/usr/bin/env python
from collections import Iterable,Iterator
import sys

#先判断对象是否为可迭代对象(Iterable)
print(isinstance('',Iterable))
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((num * num for num in range(5)),Iterable))

#再判断对象是否为迭代器(Iterator)
print(isinstance('',Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((num * num for num in range(5)),Iterator))

#对于不是迭代器的对象，可以使用iter()函数将其变为迭代器
print(isinstance(iter([]),Iterator))

#使用for循环遍历迭代器
list = [1,2,3,4]
for num in iter(list):
 print(num)

#使用next()函数遍历迭代器
list1 = [1,2,3,4]
iter = iter(list1)
while True:
  try:
    print(next(iter))
  except StopIteration:
    sys.exit()

