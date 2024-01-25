'''
150
266
427
'''
A = int(input())
B = int(input())
C = int(input())

cnt = [0] * 10
D = list(str(A * B * C))

for v in D:
    cnt[int(v)] += 1

for i in range(10):
    print(cnt[i])