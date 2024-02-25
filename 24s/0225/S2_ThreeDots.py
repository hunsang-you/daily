'''
2
5
2 0 -4 -1 4
5
1 3 2 5 4

'''
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for tc in range(T):

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = 0
    dict = defaultdict(int)

    for i in arr:
        dict[i] = 1

    for i in range(N-1):
        for j in range(i+1, N):
            temp = 2 * arr[j] - arr[i]
            if dict[temp] == 1:
                ans += 1

    print(ans)