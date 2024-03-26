'''
4 11
802
743
457
539


'''
# 이분탐색

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]
left, right = 1, max(line)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in line:
        cnt += i // mid

    if cnt >= N:
        left = mid + 1

    else:
        right = mid - 1

print(right)
