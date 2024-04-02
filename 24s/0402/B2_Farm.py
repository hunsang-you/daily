'''
3 4 9 32

3 4 8 32

100 100 2 200

'''
# 수학, 브루트포스, 사칙연산

import sys
input = sys.stdin.readline

# 양이 먹는 사료, 염소가 먹는 사료, 양과 염소의 전체수, 소비한 전체사료양
a, b, n, w = map(int, input().split())

lst = []
for i in range(1, n):
    if a * i + b * (n - i) == w:
        lst.append([i, n-i])

if len(lst) == 1:
    print(*lst[0])
else:
    print(-1)
