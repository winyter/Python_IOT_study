#!/usr/bin/env python

#基础的列表方式，实现打印任意自然数的平方
def square(input):
  list = []
  for num in range(input):
    list.append(num * num)
    print(list)
  return list
for num in square(5):
  print(num)

#生成器函数方式实现
def square1(input):
 for num in range(input):
    print('before yield')
    yield num * num
    print('after yield')
for num in square1(5):
  print(num)
