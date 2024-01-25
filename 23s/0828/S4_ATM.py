'''
5
3 1 4 3 2
'''
N = int(input())

time = list(map(int, input().split()))

time.sort()

result = 0

for i in range(1, N+1):
    result += sum(time[0:i])

print(result)