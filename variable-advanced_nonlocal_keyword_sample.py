#!/usr/bin/env python

def modify():
  num = 1
  def modify1():
    num = 2
  modify1()
  return num
print(modify())

def modify_nl():
  num = 1
  def modify1():
    nonlocal num
    num = 2
  modify1()
  return num 
print(modify_nl())
