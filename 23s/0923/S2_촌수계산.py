'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''
import sys
input = sys.stdin.readline

N = int(input())

A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(n, num) :

    num += 1
    visited[n] = 1

    if n == B:
        result.append(num)

    for i in graph[n]:
        if not visited[i]:
            print(visited)
            DFS(i, num)

DFS(A, 0)
print(graph)
if len(result) == 0:
    print(-1)

else:
    print(result[-1]-1)