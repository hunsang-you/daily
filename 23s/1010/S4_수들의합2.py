'''
4 2
1 1 1 1

10 5
1 2 3 4 2 5 3 1 1 2
'''
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while (left <= right <= N):

    total = sum(A[left:right])

    if total < M :
        right += 1

    elif total > M :
        left += 1

    elif total == M:
        cnt += 1
        right += 1

print(cnt)