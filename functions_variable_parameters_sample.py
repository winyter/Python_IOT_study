#!/usr/bin/env python

def sum(numbers):
  sum = 0
  for number in numbers:
    sum += number
  print(sum)
  return

num1 = [1,2,3,4,5]
sum(num1)

def sum_var( *numbers):
  sum = 0
  for number in numbers:
    sum += number
  print(sum)
  return

sum_var(1,2,3,4,5)
sum(1,2,3,4,5)
