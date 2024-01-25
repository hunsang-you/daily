'''
3 90 10
100 90 80

10 1 10
10 9 8 7 6 5 4 3 2 1

10 1 10
10 9 8 7 6 5 4 3 3 0

0 0 50
'''
import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())


if N == 0:
    print(1)

else :
    scores = list(map(int, input().split()))
    if N == P and scores[-1] >= new:
        print(-1)
    else:
        idx = N + 1
        for i in range(N):
            if scores[i] <= new:
                idx = i + 1
                break
        print(idx)