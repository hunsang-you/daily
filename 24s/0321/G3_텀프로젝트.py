'''
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

'''
# 그래프 이론, 탐색, DFS, BFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [0] * (N+1)
    ans = []

    def DFS(i):
        global ans
        visited[i] = 1
        team.append(i)      # 팀후보 추가
        next = arr[i]       # 다음사람

        if visited[next] == 1:
            if next in team:
                ans += team[team.index(next):]

            return
        else:
            DFS(next)

    for i in range(1, N+1):
        if visited[i] == 0:
            team = []
            DFS(i)


    print(N - len(ans))