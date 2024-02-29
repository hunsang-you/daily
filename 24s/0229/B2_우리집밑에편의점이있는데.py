'''
5 2
1 2 1 1 2
'''
# 구현

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# M개의 브랜드
brand = list(map(int, input().split()))

cnt = []

for i in range(N+1):
    cnt.append(brand.count(i))

print(max(cnt))