#!usr/bin/env python3
import math
def self_num(num):
    sum = num;
    while num > 0 :
        sum = math.trunc(sum + num % 10);
        num = num / 10;
    return sum;

if __name__ == '__main__':
    arr = [0, ]
    n = 10000
    for i in range(1, n+1):
        sum = self_num(i)
        if sum <= n:
            arr.append(sum)
    for i in range(1, n+1):
        if i not in arr:
            print("{:}".format(i))
