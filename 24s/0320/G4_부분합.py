'''
10 15
5 1 3 5 10 7 4 9 2 8

5 8
2 3 1 4 4
'''
# 누적합, 투포인터

import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

left, right = 0, 0
ans= int(1e9)
sum_ = 0
while left < right:
    if sum_ == S:
        ans = min(ans, right - left)
        sum_ -= arr[left]
        left += 1
    elif sum_ > S:
        sum_ -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum_ += arr[right]
        right += 1

if ans == int(1e9):
    print(0)

else:
    print(ans)