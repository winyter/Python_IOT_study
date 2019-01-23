#!/usr/bin/env python

dict1 = {'Messi':'169','xavi':'170','Iniesta':'171'}
print(dict1)
dict1['Messi'] = '180'
print(dict1)
dict1['Suarez'] = '182'
print(dict1)
del dict1['Suarez']
print(dict1)
dict1.clear()
print(dict1)

