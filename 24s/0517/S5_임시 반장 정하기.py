'''
5
2 3 1 7 3
4 1 9 6 8
5 5 2 4 4
6 5 2 6 7
8 4 2 2 2

'''
# 구현

import sys
input = sys.stdin.readline

N = int(input())

students = [[] for _ in range(N)]
same = [0] * N

for i in range(N):
    students[i] = list(map(int, input().split()))
    same[i] = [0] * N

for i in range(5):
    for j in range(N):
        for k in range(j + 1, N):
            if students[j][i] == students[k][i]:
                same[k][j] = 1
                same[j][k] = 1

cnt = []
for i in same:
    cnt.append(i.count(1))

print(cnt.index(max(cnt))+1)