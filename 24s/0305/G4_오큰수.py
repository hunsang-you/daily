'''
4
3 5 2 7

4
9 5 4 8
'''
# 자료구조, 스택

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

answer = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]

    stack.append(i)

print(*answer)
