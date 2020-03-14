#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter

#itemgetter() 함수를 이용하여 2개 인덱스 위치에 따라 리스트 정렬하기
my_lists = [[123,2,2,444],[22,6,6,444],[354,4,4,678],[236,5,5,678],[578,1,1,290],[461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))

#튜플 : 변경하지 못하는 리스트 같은 구조.
#괄호를 사용하여 튜플을 생성하기
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple)) # 튜플을 출력
print("Output #94: my_tuple has {} element".format(len(my_tuple))) # 튜플의 갯수 출력
print("Output #95: {}".format(my_tuple[1])) # 튜플의 2번째 인덱스를 출력
longer_tuple = my_tuple + my_tuple # 튜플을 합침.
print("Output #96: {}".format(longer_tuple)) # 합친 튜플을 출력

#튜플 풀기
one, two, three = my_tuple # my_tuple을 one = x, two = y, three = z 라는 변수를 설정해줌.
print("Output #97: {0} {1} {2}".format(one,two,three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1,var2))
#변수 간 값 교환하기
var1, var2  = var2, var1
print("Output #99: {} {}".format(var1,var2))

#튜플을 리스트로, 리스트를 튜플로 변환하기
my_list = [1,2,3]
my_tuple = ('x', 'y', 'z')
print("Output #100: {}".format(tuple(my_list))) # 리스트를 튜플로
print("Output #101: {}".format(list(my_tuple))) # 튜플을 리스트로

# 딕셔너리 : 본질적으로 고유 식별자와 쌍을 이루는 정보를 구성된 리스트를 의미
# 중괄호를 이용하여 딕셔너리 생성하기
# 각 쌍의 키와 값 사이에 콜론을 사용한다.
# len() 함수는 딕셔너리에 있는 키-값 쌍의 수를 센다.
empty_dict = { }
a_dict = { 'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements".format(len(another_dict)))

# 키를 사용하여 딕셔너리 내 특정 값에 접근하기
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))

# 복사하기
#  copy() 함수를 이용하여 딕셔너리 사본 만들기
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))

# keys(). values(), items() 를 사용하여
# 딕셔너리의 키, 값, 키-값 쌍에 접근하기 셋 다 변수 명 뒤에 입력.
print("Output #109: {}".format(a_dict. keys()))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

if 'y' in another_dict:
    print("Output #114: y is a key in another_dict: {}".format(another_dict.keys()))
if 'c' not in another_dict:
    print("Output #115: c is not a key in another_dict: {}".format(another_dict.keys()))
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four','Not in dict')))

# 정렬하기
# sorted()  함수를 이용하여 딕셔너리 정렬하기
# 우너본 딕셔너리를 수정하지 않고, 정렬하려면 먼저 사본을 만든다.
print("Output #119: {}".format(a_dict))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])


print("Output #120 (order by keys): {}".format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda  item: item[1])
print("Output #121 (order by keys): {}".format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda x:x[1], reverse = True)
print("Output #122 (order by values, ascending): {}".format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(),key=lambda x:x[1], reverse=False)
print("Output #123 (order by values, ascending): {}".format(ordered_dict4))

# if-else 문
x = 5
if x > 4 or x != 9:
    print("Output #124: {}".format(x))
else:
    print("Output #124: x is not greater than 4")

# if-elif-else 문
if x > 6:
    print("Output #125: x is greater than six")
elif x > 4 and x == 5:
    print("Output #125{}".format(x*x))
else:
    print("Output #125: x is not greater than 4")

# for루프 문
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Ang', 'Sep', 'Oct', 'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta','Holly','Isabel', 'Jenny']
print("Output #126:")
for month in y:
    print("{!s}".format(month))

print("Output #127: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1!s}".format(i,z[i]))

print("Output #128: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith(('J')): #J로 시작하는 인덱스일 경우 출력.
        print("{!s}".format(y[j]))

print("Output #129: ")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))

# 간결한 for문 :list,set, dictionary
my_data = [[1,2,3],[4,5,6],[7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #130 (list comprehension): {}".format(rows_to_keep))
