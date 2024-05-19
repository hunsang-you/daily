'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

'''
# 구현, 자료 구조, 시뮬레이션, 큐

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 1
    while arr:
        if arr[0] < max(arr):
            arr.append(arr.pop(0))

        else:
            if M == 0:
                break
            arr.pop(0)
            ans += 1

        if M > 0:
            M -= 1

        else:
            M = len(arr) - 1
    print(ans)