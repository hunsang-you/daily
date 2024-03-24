'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3


'''
# 브루트포스, 누적 합

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))
temp = [0] * (N+1)
ans = -1e9
for i in range(1, N+1):
    temp[i] = temp[i-1] + arr[i-1]


left, right = 1, K

while right < N+1:
    ans = max(ans, temp[right] - temp[left-1])
    left += 1
    right += 1

print(ans)