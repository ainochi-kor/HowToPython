#!/usr/bin/env python3

string = input()
alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
                   'o','p','q','r','s','t','u','v','w','x','y','z']

for index in range(0,len(string)):
    count = -1;
    for i in alpabet:
        count += 1
        if i == string[index]:
            alpabet[count] = index
            break

for i in range(0,len(alpabet)):
    try:
        if ord(alpabet[i]) > 65:
            print(-1, end=' ')
    except:
        print(alpabet[i], end=' ')



