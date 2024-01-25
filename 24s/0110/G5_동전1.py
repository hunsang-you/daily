'''
3 10
1
2
5
'''
# DP

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1

for i in coins:
    for j in range(1, K+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[K])