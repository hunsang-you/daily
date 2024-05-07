'''
baekjoon

'''
# 문자열, 정렬

import sys
input = sys.stdin.readline

word = input().rstrip()
lst = []

for i in range(len(word)):
    lst.append(word[i:])

lst.sort()

for i in lst:
    print(i)