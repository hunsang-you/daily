'''
1

19

500000


'''
# 브루트포스 알고리즘, 백트래킹

import sys
input = sys.stdin.readline

N = int(input())

result = set()

number = []

def DFS():
    if number:
        result.add(int(''.join(map(str, number))))

    for i in range(10):
        if not number or number[-1] > i:
            number.append(i)
            DFS()
            number.pop()

DFS()

result = sorted(result)

if len(result) >= N:
    print(result[N-1])

else:
    print(-1)