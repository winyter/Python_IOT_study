#!/usr/bin/env python

try:
  print('try...')
  x = 2/0
  print(x)
except ZeroDivisionError as e:
  print('except:',e)
finally:
  print('finally...')
print('exit...')
