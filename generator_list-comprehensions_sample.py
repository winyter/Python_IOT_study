#!/usr/bin/env python

#基础for循环实现1~10的平方计算

list1 = []
for num in range(1,11):
  list1.append(num * num)
print(list1)

#列表推导式实现1~10的平方计算

list2 = [num * num for num in range(1,11)]
print(list2)

#其他列表推导式举例

#实现打印1~10所有偶数平方
list3 = [num * num for num in range(2,11,2)]
print(list3)
#另一种写法
list4 = [num * num for num in range(1,11) if num % 2 ==0]
print(list4)

#实现两个列表的全排列，可以理解为双循环

list5 = ['a','b','c']
list6 = ['1','2','3']
list7 = [char+num for char in list5 for num in list6]
print(list7)
