'''
123 45

'''
# 수학, 구현, 문자열

import sys
input = sys.stdin.readline

A, B = map(str, input().split())
A, B = list(map(int, A)), list(map(int, B))
ans = 0


print(sum(A) * sum(B))
