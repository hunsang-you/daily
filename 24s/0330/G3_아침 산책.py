'''
5
10111
1 2
2 3
2 4
4 5


'''
# 수학, 그래프 이론, 탐색, 트리, 조합론, DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def DFS(n, cnt):
    visited[n] = 1

    for v in graph[n]:
        # 인접한 노드가 실내라면
        if arr[v] == '1':
            cnt += 1

        elif visited[v] == 0 and arr[v] == '0':
            cnt = DFS(v, cnt)
    return cnt

N = int(input())
# 1 = 실내    0 = 실외
arr = [-1] + list(str(input().rstrip()))
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
twin = 0
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    # 실내 두개가 연결되어 서로 방문하는 경우
    if arr[u] == '1' and arr[v] == '1':
        twin += 2

ans = 0
# 실내인 곳을 시작
for i in range(1, N+1):
    if arr[i] == '1' and visited[i] == 0:
        temp = DFS(i, 0)
        ans += (temp) * (temp-1)

print(ans+twin)