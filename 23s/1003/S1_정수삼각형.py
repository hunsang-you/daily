'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''
# DP
'''
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
'''
# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
'''
dp[0][0] = 7
dp[1][0] = 7 + 3  dp[1][1] = 7 + 8
dp[2][0] = 7 + 3 + 8  dp[2][1] = 7 + 8 + 1  dp[2][2] = 7 + 8 + 0
dp[3][0] = 7 + 3 + 8 + 2  dp[3][1] = 7 + 8 + 1 + 7   dp[3][2] = 7 + 8 + 0 + 4  dp[3][3] = 7 + 8 + 0 + 4

'''
import sys
input = sys.stdin.readline

N = int(input())
tree = []
for i in range(N):
    tree.append(list(map(int, input().split())))

dp = tree
for i in range(1, N):
    for j in range(len(tree[i])):
        if j == 0 :
            dp[i][j] = tree[i][j] + tree[i-1][j]
        elif j == len(tree[i])-1:
            dp[i][j] = tree[i][j] + tree[i-1][j-1]
        else:
            dp[i][j] = max(tree[i-1][j-1], tree[i-1][j]) +tree[i][j]
        # print(dp)
print(max(dp[-1]))