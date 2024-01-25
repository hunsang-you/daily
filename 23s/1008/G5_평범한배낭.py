'''
4 7
6 13
4 8
3 6
5 12
'''
# DP
# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0,0]]
dp = [[0] * (K+1) for _ in range(N+1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        W = stuff[i][0]
        V = stuff[i][1]

        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)

print(dp[N][K])