'''
0 1 2 2 2 7

2 1 2 1 2 1
'''
# 브루트포스, 사칙연산

K, Q, R, B, N, P = map(int, input().split())

print(1-K, 1-Q, 2-R, 2-B, 2-N, 8-P, end=" ")