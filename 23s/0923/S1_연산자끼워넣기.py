'''
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''

# DFS
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

# + - * / 순서
op = list(map(int, input().split()))
# arr =[0] * (N + (N-1))

maxNum = -1e9
minNum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maxNum, minNum
    if depth == N:    # 연산자를 다썼다면
        maxNum = max(total, maxNum)
        minNum = min(total, minNum)
        return

    if plus:
        dfs(depth + 1, total + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - A[depth], plus , minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * A[depth], plus , minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(total / A[depth]), plus , minus, multiply, divide-1)

dfs(1, A[0], op[0],op[1], op[2], op[3])
print(maxNum)
print(minNum)
