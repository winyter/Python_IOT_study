#!/usr/bin/env python

from functools import reduce

#通过reduce()实现简单的累加
numbers = [1,2,3,4,5]
def f(x,y):
  return x+y
print(reduce(f,numbers))
print(sum(numbers))

#带有初始值的reduce()的用法
print(reduce(f,numbers,10))

#实现累乘的用法
def h(x,y):
  return x * y
print(reduce(h,numbers))
