'''
2

10
'''
# DP, 그래프이론, 그래프탐색

N = int(input())
dp = [0] * (N+1)
history = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    history[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        history[i] = i // 3

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        history[i] = i // 2

print(dp[N])
print(N, end=" ")

temp = N
while history[temp] != 0:
    print(history[temp], end=' ')
    temp = history[temp]