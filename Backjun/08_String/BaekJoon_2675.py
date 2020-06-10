#!/usr/bin/env python3

line = int(input())

for i in range(0,line):
    cycle, char_line = input().split()
    for j in range(0,len(char_line)):
        for k in range(0,int(cycle)):
            print(char_line[j],end="")
    print("")
