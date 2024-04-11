'''
15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5

1
10

4
5 5 5 5

5
1 2 7 3 2

10
1000000000 999999999 999999998 999999997 999999996 1 2 3 4 5

'''
# 수학, 브루트포스, 기하학

import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N

for i in range(N-1):
    temp = -1e9
    for j in range(i+1, N):
        slope = (arr[j] - arr[i]) / (j - i)     # 높이증가량 / 거리증가량 => 기울기
        if slope > temp:
            temp = max(temp, slope)
            ans[i] += 1
            ans[j] += 1

print(max(ans))


