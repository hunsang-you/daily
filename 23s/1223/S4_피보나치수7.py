'''
10

1000
'''
# DP

N = int(input())
fir, sec = 0, 1

for i in range(N):
    fir, sec = (fir + sec) % 1000000007, fir % 1000000007

print(fir)
