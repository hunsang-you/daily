'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
# 자료구조
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
arr = [i for i in range(n+1)]


def find_arr(x):
    if arr[x] != x:
        arr[x] = find_arr(arr[x])
    return arr[x]

def union_arr(a, b):
    a = find_arr(a)
    b = find_arr(b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_arr(a, b)

    else:
        if find_arr(a) == find_arr(b):
            print('YES')
        else :
            print('NO')