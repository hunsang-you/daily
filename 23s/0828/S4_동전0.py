'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
N, K = map(int, input().split())
money = []
cnt = 0
for _ in range(N):
    money.append(int(input()))

money.reverse()

for i in range(N):
    cnt += K // money[i]
    K = K % money[i]

print(cnt)