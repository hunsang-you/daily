'''
3 1
4 4 2

4 2
9 7 9 1

4 4
1 1 2 2
'''

N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def func(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(idx, N):
        if not visited[i] and overlap != L[i]:
            out.append(L[i])
            visited[i] = True
            overlap = L[i]
            func(depth+1, i+1, N, M)
            out.pop()
            visited[i] = False

func(0, 0, N, M)