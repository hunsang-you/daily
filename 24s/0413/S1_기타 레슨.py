'''
9 3
1 2 3 4 5 6 7 8 9

'''
# 이분탐색, 매개변수탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)
ans = 0
while start <= end:
    mid = (start + end) // 2

    temp = 0
    cnt = 1

    for time in arr:
        if temp + time > mid:
            cnt += 1
            temp = 0
        temp += time

    if cnt <= M:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)