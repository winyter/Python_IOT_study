#!/usr/bin/env python

#通过简单的筛选1~10之间所有的奇数，来说明filter()函数的原理与用法，即filter()函数会将指定的序列一一带入指定的函数，通过true和false的判断，实现对序列的筛选
numbers = range(1,11)
def f(x):
  return x%2 == 1
odds = filter(f,numbers)
print(list(odds))

#实现删除一个序列中的所有空字符串
old_strs = ['messi','   ','xavi','',None]
print(old_strs)

def f(x):
  return x and x.strip()	#需要注意，该句运用到一个逻辑与and运算的窍门，即(0,'',[],(),{},None,False) and 任何数都为假,strip()方法可以删除字符串首尾指定的字符，默认为空格或换行符
new_strs = filter(f,old_strs)
print(list(new_strs))

