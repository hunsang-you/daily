'''
1 285
150 50 10

1 123456
123456 10000 1

3 1
270758 196 67
904526 8930 66
121164 3160 56

3 1000000
718571 2557 74
480573 9706 54
16511 6660 90

5 395439
407917 8774 24
331425 4386 58
502205 9420 32
591461 1548 79
504695 8047 53

'''
# 이분탐색, 브루트포스, 수학

import sys
input = sys.stdin.readline

N, T = map(int, input().split())

result = []
for _ in range(N):
    S, I, C = map(int, input().split())

    lst = [S + (I * i) for i in range(C)]
    if lst[-1] < T:
        continue

    left, right = 0, C-1
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] >= T:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    result.append(lst[ans]-T)

if result:
    print(min(result))
else:
    print(-1)