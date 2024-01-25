'''
3
2 3 1

4
2 1 3 1

8
4 1 6 1 3 6 1 4
'''
import sys
input = sys.stdin.readline

A = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

ans = []

for i in range(A):
    idx = sorted_arr.index(arr[i])
    ans.append(idx)
    sorted_arr[idx] = -1

for i in range(A):
    print(ans[i], end=" ")

