'''
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
'''
# 정렬 이분탐색 투 포인터

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    cnt = 0

    start = 0

    for i in range(N):
        while True:

            if start == M or A[i] <= B[start]:
                cnt += start
                break
            else:
                start += 1
    print(cnt)