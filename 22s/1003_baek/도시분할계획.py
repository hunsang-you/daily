'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
def find(x):
    if x == parents[x] :
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parents[a] = b
    else:
        parents[b] = a

N, M = map(int, input().split())
graph = []
parents = list(range(N+1))

for _ in range(M):
    a, b, weight = map(int, input().split())
    graph.append((weight, a, b))


graph.sort(key=lambda x:x[0])

result = 0
cnt = 0
for w, x, y in graph:
    if find(x) != find(y):
        union(x, y)
        result += w
        cnt += 1
        if cnt >= N-2:
            break

print(result)