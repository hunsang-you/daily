'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
'''

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

dp = [0] * (N+1)
for i in range(1, N+1):
    T, P = data[i-1][0], data[i-1][1]

    if i + T -1 <= N :
        dp[i+T-1] = max(dp[i+T-1], dp[i-1] + P)
    if dp[i] < dp[i-1] :
        dp[i] = dp[i-1]

print(max(dp))