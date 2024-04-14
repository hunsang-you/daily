'''
5
1
5
3
1
2

'''
# 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline

N = int(input())

arr = [0] + [int(input()) for _ in range(N)]
arr.sort()

ans = 0

for i in range(1, N+1):
    ans += abs(i - arr[i])
print(ans)