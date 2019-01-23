#!/usr/bin/env python

for char in 'one':
  if 'n' == char:
    break
  print(char)

num = 1
while num > 0:
  print(num)
  num += 1
  if 2 == num:
    break
print('exit')
