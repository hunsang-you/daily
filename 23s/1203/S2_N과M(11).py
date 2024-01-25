'''
3 1
4 4 2

4 2
9 7 9 1

4 4
1 1 2 2
'''
# 백트래킹

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
result = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    temp = 0
    for i in range(N):
        if temp != lst[i]:
            result.append(lst[i])
            temp = lst[i]
            solve(depth+1, N, M)
            result.pop()

solve(0, N, M)