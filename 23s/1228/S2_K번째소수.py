'''
1

3
'''

INF = 10 ** 7
lst = [1] * INF

for i in range(2, int(INF ** 0.5) +1):
    if lst[i]:
        for j in range(i+i, INF, i):
            lst[j] = 0

prime = []
K = int(input())
for i in range(2, INF):
    if lst[i]:
        prime.append(i)
print(prime[K-1])
