'''
6
10
20
15
25
10
20
'''
# DP
# 계단을 밟으면 그 점수를 획득
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * N
dp = [0] * N
for i in range(N):
    stairs[i] = int(input())

if len(stairs) <= 2:
    print(sum(stairs))

else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[-1])

