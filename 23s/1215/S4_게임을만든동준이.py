'''
3
5
5
5

4
5
3
7
5
'''
# 그리디

import sys
input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]

answer = 0
for i in range(N-2, -1, -1):
    if scores[i] >= scores[i+1]:
        answer += scores[i] - scores[i+1] + 1
        scores[i] = scores[i+1]-1


print(answer)