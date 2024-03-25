'''
1
5
4 1 5 2 3
5
1 3 7 9 5


'''
# 이분탐색

import sys
input = sys.stdin.readline

T = int(input())

def binary_search(l, r, arr1, num):
    while l <= r:
        mid = (l + r) // 2

        if arr1[mid] == num:
            return 1

        elif arr1[mid] < num:
            l = mid + 1

        else:
            r = mid - 1
    return 0

for _ in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr1.sort()
    M = int(input())
    arr2 = list(map(int, input().split()))
    left, right = 0, N-1

    for num in arr2:
        print(binary_search(left, right, arr1, num))