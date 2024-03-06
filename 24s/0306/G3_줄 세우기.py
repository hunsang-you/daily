'''
3 2
1 3
2 3

4 2
4 2
3 1
'''
# 그래프 이론, 위상정렬, 방향 비순환 그래프

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
students = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
queue = deque()
answer = []
for _ in range(M):
    # A가 B보다 앞에 선다(A < B)
    A, B = map(int, input().split())
    students[A].append(B)
    check[B] += 1       # B보다 작은 학생수

for i in range(1, N+1):
    if check[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    answer.append(now)

    # 현재 학생보다 큰 학생 i
    for i in students[now]:
        check[i] -= 1
        if check[i] == 0:
            queue.append(i)
print(*answer)