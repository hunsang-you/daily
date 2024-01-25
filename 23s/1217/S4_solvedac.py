'''
5
1
5
5
7
8

10
1
13
12
15
3
16
13
12
14
15
'''

import sys
input = sys.stdin.readline

def roundfunc(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
answer = 0
if N > 0:
    people = [int(input()) for _ in range(N)]
    people.sort()
    temp = roundfunc(N*0.15)

    if temp > 0:
        answer = roundfunc(sum(people[temp:-temp]) / len(people[temp:-temp]))

    else:
        answer = roundfunc(sum(people) / len(people))

print(answer)
