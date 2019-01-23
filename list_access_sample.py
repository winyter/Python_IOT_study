#list_sample.py
#!/usr/bin/env python

list1 = ['Python',123,22.5]
list2 = [55,'IoT']

print(list1)
print(list1[0])
print(list1[-1])
print(list1[1:])
print(list2 * 2)
print(list1 + list2)
list2[1] = 'new'
print(list2)

