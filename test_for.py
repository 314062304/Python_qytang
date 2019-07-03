#!/usr/local/bin/python3
# # -*- coding: UTF-8 -*-

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# 不使用函数
print('方案一')
for i in list1:
    if i in list2:
        print(i, 'in List1 and List2')
    else:
        print(i, 'only in List1')


# 使用函数
print('\n')
print('方案二')
def intersect(list1, list2):
    for a in list1:
        if a in list2:
            print(a, 'in List1 and List2')
        else:
            print(a, 'only in List1')

intersect(list1, list2)

