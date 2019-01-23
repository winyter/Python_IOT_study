#!/usr/bin/env python

#字典键名必须唯一，多次使用同一个键，系统只会记住最后一个定义的值

dict1 = {'messi':'169','xavi':'170','messi':'171'}
print(dict1)

#值不限数据类型，但一个字典内，所有键必须为不可变的数据类型，如字符串、数字或元组，不可以是列表这类可变数据类型

dict2 = {'messi':'169',1:1,('xavi'):'171'}
print(dict2)
dict2 = {'messi':'169',('xavi'):'171',['list1']:'list1'}
