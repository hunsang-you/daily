N = int(input())
num = [1, 5, 10, 50]
result = []
for i in range(N+1):
    for j in range(N+1 -i):
        for k in range(N+1-i-j):
            temp = N - i - j - k
            number = i + 5 * j + 10 * k + 50 * temp
            result.append(number)

if N == 0:
    print(0)
    exit(0)


ans = set(result)
print(len(ans))