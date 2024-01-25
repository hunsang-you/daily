'''
5
-2 4 -99 -1 98
'''
# 투포인터, 이분탐색

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

left, right = 0, N-1

answer = abs(lst[left] + lst[right])
res = [lst[left], lst[right]]
while left < right :
    val_l = lst[left]
    val_r = lst[right]

    SUM = val_l + val_r

    if abs(SUM) < answer:
        answer = abs(SUM)
        res = [val_l, val_r]
        if answer == 0:
            break
    if SUM < 0:
        left += 1

    else:
        right -= 1

print(res[0], res[1])
