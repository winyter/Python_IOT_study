#!/usr/bin/env python

test1 = {1,2,3,4}
print('test1:',test1)

test1.add(5)
print('test1:',test1)
test1.update([6,7])
print('test1:',test1)
test1.remove(7)
print('test1',test1)
print(len(test1))
print(6 in test1)
test1.clear()
print(test1)
del test1
print(test1)

