'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

N = int(input())                    # 정점의 수
pair = int(input())                 # 간선의 수
graph = [[] * N for _ in range(N+1)]        # 각 숫자끼리 연결되있는 리스트 표현

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (N+1)

def bfs(s):
    global cnt
    visited[s] = 1
    queue = [s]
    while queue :
        for i in graph[queue.pop()]:
            if visited[i] == 0:
                visited[i] = 1
                queue.insert(0, i)          # insert(a,b) a번째 위치에 b를 삽입
                cnt += 1

bfs(1)
print(cnt)