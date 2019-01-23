#assemble_sample.py
#!/usr/bin/env python

test = {'one','two','one','three'}
print(test)
pool = 'abcdefgaaabbc'
test1 = set(pool)
print(pool)
print(test1)
test2 = set('abcdg')
print(test2)
test3 = set()
print(test3)
print(test)
if('one' in test):
  print('one is in test')
else:
  print('one is not in test')
print(test1 - test2)	#差集，1有2无
print(test2 - test1)	#差集，2有1无,如果减出来是空集，则显示为set()，如本例所示
print(test1 | test2)	#并集
print(test1 & test2)	#交集
print(test1 ^ test2)	#对称差集，即不同时在两个集合中出现的元素

