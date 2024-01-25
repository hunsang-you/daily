'''
8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4
'''
# DP, 브루트포스

N = int(input())
num = [float(input()) for _ in range(N)]

for i in range(1, N):
    num[i] = max(num[i], num[i] * num[i - 1])

print('%0.3f' % max(num))