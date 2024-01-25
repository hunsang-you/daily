'''
6
'''
# DP

N = int(input())

dp = [0] * (N+5)
# 0 -> 창근승 1 -> 상영승
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 1

for i in range(5, N+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N] == 1:
    print('SK')
else:
    print('CY')
