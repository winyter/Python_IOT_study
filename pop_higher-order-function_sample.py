#!/usr/bin/env python
#函数作为参数传入函数，此为高阶函数

def plus(num1,num2,func):
  return func(num1) + func(num2)
print(plus(-3,-4,abs))
