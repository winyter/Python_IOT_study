#!/usr/bin/env python

list1 = [num * num for num in range(1,6)]	#列表推导式
generator1 = (num * num for num in range(1,6))	#生成器表达式

print(list1)
print(generator1)

print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
