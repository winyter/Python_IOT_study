#!/usr/bin/env python

#首先简单实现一个列表每个整数的平方计算，以来说明一下map()函数是将一个函数作用在一个可迭代对象上，并生成一个新的可迭代对象这一原理

old_list = [1,2,3,4,5]
print(old_list)

def f(x):
  return x * x

new_iter = map(f,old_list)	#python 3.x 中map()返回的是一个迭代器
new_list = list(new_iter)
print(new_list)			#map函数生成的迭代器可以使用list()函数转换为list直接打印
print(old_list)

#然后实际应用一下map()函数，实现将乱输的英文名转换为标准的首字母大写的英文名

bad_name = ['mESsI','XAvI','iNiEStA']
print(bad_name)
def CorrectName(name):
  return (name.lower().capitalize())	#low()：字符串转换为小写，capitalize()：字符转首字母转换为大写
good_name = map(CorrectName,bad_name)
print(list(good_name))

