'''
5 4
1 2
3 4
1 4
2 2

'''
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]1
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)
