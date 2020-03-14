#!/usr/bin/env python3
from math import exp, log, sqrt

'''
라이브러리 math에서 exp,log, sqrt를 가져옴.
exp : e의 거듭제곱
log : 자연로그
sqrt : 제곱근
'''

print("p48 e의 거듭제곱, 자연로그, 제곱근")
print("Output #11: {0:.4f}".format(exp(3))) #e의 거듭제곱을 의미함.
print("Output #12: {0:.2f}".format(log(4))) #자연로그
print("Output #13: {0:.1f}".format(sqrt(81))) #제곱근

print("\np.48 문자열")
print("Output #14: {0:s}".format('I\'m enjoying learning python.'))
print("Output #15: {0:s}".format("This is a long string. Without the backslash"
                                 "it would run off of the page on the right in the text editor and be very"
                                 "difficult to read and edit. By using the backslash you can split the long"
                                 "string into smaller strings on separate lines so that the whole string is easy"
                                 "to view in the text editor."))
print("Output #16: {0:s}".format('''You can use triple single quotes for multi-line commit strings.'''))
print("Output #17: {0:s}".format("""You can also use triple double quotes for multi-line comment strings"""))
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s} {2:s}".format("She is","very"*4,"beautiful."))
m = len(sentence) # len은 공백문자나 마침표 등을 포함하여 문자열 길이를 샌다.
print("Output #20: {0:d}".format(m))

print("\np.51 split")
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: First piece:{0}, Second piece:{1} Thrid piece{2}".format(string1_list2[0],string1_list2[1],string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1],string2_list[5],string2_list[-1]))

print("\np.52 join")
#문자열을 결합할 떄 쓰는 함수.
print("Output #25: {0}".format(','.join(string2_list)))


print("\np52.strip / lstrip / rstrip")
#공백문자, 개행문자 등을 삭제할 때 사용.
string3 = " Remove unwanted characters from this stirng.\t\t   \n"
print("Output #26: strip3: {0:s}".format(string3))
string3_lstrip =  string3.lstrip()
print("Output #27: lstrip3: {0:s}".format(string3_lstrip))
string3_rstrip =  string3.rstrip()
print("Output #28: rstrip3: {0:s}".format(string3_rstrip))
string3_strip =  string3.strip()
print("Output #29: strip3: {0:s}".format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__---++ "
print("Output #30: {0:s}".format(string4))
string4 = "$$The nuwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

print("\np.53 replace")
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #33 (with commas): {0:s}".format(string5_replace))

print("\np52. lower, upper, capitalize")
'''
    lower : 모두 소문자로 치환
    upper : 모두 대문자로 치환
    capitalize : 첫번째 문자열에만 Upper를 적용하고 나머진 다 lower를 적용함.
'''
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when YOu Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize"
print("Output #36: {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #37: on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))
