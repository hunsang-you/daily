'''
3
1 2 3

'''
# 구현

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lst = [0] * 101
ans = 0
for i in arr:
    if lst[i] == 0:
        lst[i] = 1

    elif lst[i] == 1:
        ans += 1
print(ans)