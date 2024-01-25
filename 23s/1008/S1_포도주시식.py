'''
6
6
10
13
9
8
1
'''
# DP
# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.



N = int(input())
wine = [0] * 10000
for i in range(N):
    wine[i] = int(input())
dp = [0] * 10000

dp[0] = wine[0]
dp[1] = wine[1] + wine[0]
dp[2] = max(wine[0] + wine[2], wine[2] + wine[1], dp[1])


for i in range(3, N):
    dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])
print(max(dp))