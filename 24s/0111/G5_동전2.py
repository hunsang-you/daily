'''
3 15
1
5
12
'''
# DP

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [10001] * (K+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i-coin]+1, dp[i])

if dp[K] == 10001:
    print(-1)

else:
    print(dp[K])