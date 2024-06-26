'''
4
1 2 3 4

5
5 4 3 2 1

'''
# 수학, 조합론

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if arr[i-1] < arr[i]:
        for j in range(N-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                print(" ".join(map(str, arr)))
                exit()

print(-1)