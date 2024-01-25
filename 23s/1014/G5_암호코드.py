'''
25114

1111111111
'''
# DP


N = list(map(int, input()))
L = len(N)
dp = [0 for i in range(L+1)]

if (N[0] == 0):
    print("0")

else:
    N = [0] + N
    dp[0] = 1
    dp[1] = 1
    for i in range(2, L+1):
        if N[i] > 0:
            dp[i] += dp[i-1]
        tmp = N[i-1] * 10 + N[i]
        if 10 <= tmp and tmp <= 26:
            dp[i] += dp[i-2]

    print(dp[L] % 1000000)