'''
5 5
1 3
1 4
4 5
4 3
3 2
'''
from collections import deque
def BFS(V):
    visited = [0] * (N+1)       # visited는 시작 숫자가 바뀔때마다 초기화 되어야 한다.
    queue = deque()
    queue.append(V)
    visited[V] = 1      # 첫 시작 방문을 1
    while queue:
        pre = queue.popleft()
        for next in graph[pre]:       # V에 연결되있는 요소 next가 방문되지 않았다면 이전 방문했던 값에 +1 하여 바꿔준다.
            if visited[next] == 0:
                visited[next] = visited[pre] + 1
                queue.append(next)
    return sum(visited)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):                  # 그래프 형성
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

bacon_lst = []
for i in range(1, N+1):         # 리스트에 함수를 통해 각 숫자의 베이컨값을 추가
    bacon_lst.append(BFS(i))

# print(bacon_lst)
result = bacon_lst.index(min(bacon_lst))    # 최소값이 있는 인덱스(0부터 시작이므로 +1을 해준다)

print(result+1)