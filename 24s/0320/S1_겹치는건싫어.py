'''
9 2
3 2 5 5 6 4 4 5 7

10 1
1 2 3 4 5 6 6 7 8 9

'''
# 투 포인터

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * (max(arr) + 1)
left, right = 0, 0

ans = 0
while right < N:
    # right번째의 숫자가 K보다 작다면 count를 + 1
    if count[arr[right]] < K:
        count[arr[right]] += 1
        right += 1

    else:
        count[arr[left]] -= 1
        left += 1

    ans = max(ans, right - left)

print(ans)

