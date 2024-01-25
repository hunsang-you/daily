'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''
def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(a, b):
    a = find_set(a)
    b = find_set(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
M = int(input())
edges = []
parent = list(range(N+1))


for _ in range(M):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort(key=lambda x:x[0])

result = 0xffffffff

sumV = 0
for w, s, e in edges:
    if find_set(s) != find_set(e):
        union(s, e)
        sumV += w

print(sumV)