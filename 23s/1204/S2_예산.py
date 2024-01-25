'''
4
120 110 140 150
485

5
70 80 30 40 100
450
'''
# 이분탐색
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

def func(lst):
    start = 0
    end = max(lst)

    while start <= end:
        center = (start + end) // 2
        cnt = 0

        for i in range(N):
            if lst[i] >= center:
                cnt += center

            else :
                cnt += lst[i]
        if cnt <= M:
            start = center + 1

        else:
            end = center - 1
    return end

print(func(lst))