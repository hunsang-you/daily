'''
ACAYKP
CAPCAK
'''
# DP

import sys
input = sys.stdin.readline

word1 = input()
word2 = input()
r = len(word1)
c = len(word2)
dp = [[0] * (c) for _ in range(r)]

for i in range(1, r):
    for j in range(1, c):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
