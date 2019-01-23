#!/usr/bin/env python

num = 1
def modify():
  global num
  num = 2
  return num
modify()
print(num)

