'''
3 3
1 2 1
2 3 2
1 3 3
'''
# 크루스칼
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


V, E = map(int, input().split())
edges = []
for _ in range(E):
    A, B, W = map(int, input().split())
    edges.append((W, A, B))

edges.sort(key=lambda x:x[0])

parent = list(range(V+1))

sumV = 0
for w, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        sumV += w

print(sumV)