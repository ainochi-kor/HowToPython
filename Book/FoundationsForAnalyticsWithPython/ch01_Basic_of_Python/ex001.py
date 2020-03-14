#!/usr/bin/env python3
print("p.34")
print("Output #1: I'm excited to learn Python.\n")

print("p.41~42")
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.\n".format(z))

print("p.42")
# 두 리스트를 더한다.
a = [1,2,3,4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a,b,c))
print("\n")

print("p.46 정수")
x = 9
print("Output #4: {0}".format(x)) # x에 할당하기
print("Output #5: {0}".format(3**4)) #3을 4제곱
print("Output #6: {0}".format(int(8.4)/int(2.7))) #정수형 변환
print("\n")

print("p.46 실수")
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5 * 4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))
print("\n")
