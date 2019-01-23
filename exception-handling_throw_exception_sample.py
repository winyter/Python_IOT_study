#!/usr/bin/env python

class IoTError(ValueError):
  pass
def func(input):
  num = int(input)
  if 0 == num:
    raise IoTError('Invalid value: %s' % input)
    return 2/num
func('0')

