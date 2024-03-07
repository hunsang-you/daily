'''
3 2
2 3
1 2

6 4
1 2
1 3
2 5
4 5
'''
# 다이나믹 프로그래밍, 그래프이론, 위상정렬, 방향 비순환 그래프
# A과목이 B과목의 선수과목

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
subject = [1] * (N+1)

check = []


for i in range(M):
    A, B = map(int, input().split())
    check.append((A, B))

check.sort()

for p, n in check:
    if subject[n] <= subject[p]:
        subject[n] = subject[p] + 1

for i in range(1, N+1):
    print(subject[i], end=" ")


