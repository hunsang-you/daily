'''
4
1 4 0 1

5
1 6 3 8 3

3
0 100 0

1
0
'''

import sys
input = sys.stdin.readline
N = int(input())

S = [0] + list(map(int, input().split()))

arr = [0] * len(S)

for i in range(1, N+1):
    if S[i] > 0 :
        arr[i] = arr[i-1] + 1

print(max(arr))

