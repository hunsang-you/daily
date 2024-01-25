N, K = map(int, input().split())
ans = 1
for i in range(K):
    ans *= (N - i)

for i in range(1, K+1):
    ans /= i

print(round(ans))