'''
7 7 7
6 5 4
3 2 5
6 2 6
0 0 0
'''

import sys
input = sys.stdin.readline


while True:
    lst = sorted(list(map(int, input().split())))
    if lst[0] == lst[1] == lst[2] == 0:
        break
    if lst[0]+lst[1] <= lst[2]:
        print("Invalid")
    elif lst[0] == lst[1] == lst[2]:
        print("Equilateral")
    elif lst[0]==lst[1] or lst[1]==lst[2] or lst[2]==lst[0]:
        print("Isosceles")
    else:
        print("Scalene")