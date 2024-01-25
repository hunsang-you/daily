M = int(input())
N = int(input())

sqrt = []

for num in range(M, N+1):
    root = int(num ** 0.5)
    if num == root ** 2 :
        sqrt.append(num)

if sqrt == []:
    print(-1)
else:
    print(sum(sqrt))
    print(min(sqrt))