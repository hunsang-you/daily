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

# 각 숫자의 인덱스에 연결되있는 숫자를 추가       // [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (N+1)               # 방문 여부를 확인할 0으로 이루어진 리스트 생성

def dfs(s):
    global cnt
    visited[s] = 1              # 처음 시작할 때 1로 바꾸고
    for i in graph[s]:          # graph[s]에 대한 i값에 대해
        if visited[i] == 0:     # visited[i]가 0이라면 dfs함수를 반복한다.
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)

