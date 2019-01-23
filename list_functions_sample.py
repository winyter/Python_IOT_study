#!/usr/bin/env python

list = [1,2,3,4,'Python']
print(list)
print('len():',len(list))

listNum = [1,2,3,4]
print('max():',max(listNum))  #max()和min()仅支持全是数字的list，如果有非数字的元素，python会报错
print('min():',min(listNum))

list.append('IoT')
print('after append():',list)
list.remove('IoT')
print('after remove():',list)
list.reverse()
print('after reverse():',list)

list1 = [1,2,1,3,1,3,2,1]
print(list1)
print('count 1:',list1.count(1))
print('count 2:',list1.count(2))
print('count 3:',list1.count(3))


