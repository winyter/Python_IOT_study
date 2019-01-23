#!/usr/bin/env python

b_num = int(1.5)	#内建作用域(Built-in)
g_num = 2		#全局作用域(Global)
def out_func():
  e_num = 3		#闭包函数外的函数作用域(Enclosing)
  def in_func():
    l_num = 4		#局部作用域(Local)
    return l_num
  print('L:',in_func())
  return e_num
print('E:',out_func())
print('G:',g_num)
print('B:',b_num)
