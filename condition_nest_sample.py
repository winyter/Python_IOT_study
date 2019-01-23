#condition_nest_sample.py
#!/usr/bin/env python

var = int(input('Please input a number from 1 to 4:'))
if var > 2:
  if var > 3:
    print('input number is 4')
  else:
    print('input number is 3')
elif var < 2:
  print('input number is 1')
else:
  print('input number is 2')

