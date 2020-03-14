#리스트를 만들기 위해 대괄호를 사용한다
# len() 함수를 통해 리스트 내 원소의 수를 센다.
# max()함수와 min() 함수는 최대/최소 값을 찾는다.
# count() 함수는 리스트 내 특정 값이 등장한 횟수를 센다
a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list))) #원소수의 개수를 셈.
print("Output #60: the maximum value in a_list is {}".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}".format(min(a_list)))
another_list = ['printer', 5 , ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5))) #count는 값의 등장 횟수를 센다.

# 리스트 내 특정 원소에 접근하려면 인덱스 이용하기
# [0]은 첫 번째 원소이다. [-1]은 마지막 원소이다.
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

# 리스트 분할을 사용하여, 리스트 원소들의 부분집합 만들기
# 맨 앞부터 분할하는 경우, 최초 인덱스를 생략한다.
# 맨 뒤부터 리스트를 분할하는 경우, 마지막 인덱스는 생략한다.
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[0:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

# [:]를 이용하여 리스트 복사하기
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))


# + 연습자를 이용하여 2개 이상의 리스트를 병합하기
a_longer_list = a_list + another_list
print(("Output #78: {}".format(a_longer_list)))

# in과 not in을 이용하여 특정 원소의 리스트
# 들어있는지 아닌지 true / false로 확인하는 작업.
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}".format(a_list))

# append() 함수를 이용하여 리스트의 마지막에 원소를 추가하기.
# remove() 함수를 이용하여 리스트 내 특정 원소를 제거하기.
# pop() 함수를 이용하여 리스트의 마지막 원소를 제가하기.

a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# reverse() 함수를 이용하여 리스트 반전하기
# 해당 리스트 내에서 (인플레이스) 변경이 일어나므로
# 기존 리스트를 변경하지 않고 반전하려면 먼저 사본을 만들어둬야 한다.

a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

# sort() 함수를 이용하여 리스트를 인플레이스로 정렬하기
# 이는 리스트가 변경된다는 것을 의미한다.
# 기존 리스트의 변경 없이 리스트를 정렬하려면, 우선 사본을 만든다
unordered_list = [3,5,1,7,2,8,4,9,0,6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# sorted() 함수를 이용하여 리스트들의 특정 위치에 따라 리스트 정렬하기
# lambda 함수는 지정된 값에 의한 정렬을 함.
my_lists = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_list_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_list_sorted_by_index_3))
