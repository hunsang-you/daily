'''
7 3
'''
N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
res = []
number = 0

for i in range(N):
    number += (K-1)
    if number >= len(arr):
        number %= len(arr)

    res.append(str(arr[number]))
    arr.pop(number)


print("<",', '.join(res), ">", sep="")