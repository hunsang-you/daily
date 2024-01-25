'''
4
2 1 1 0
5
0 0 0 0 0
6
5 4 3 2 1 0
7
6 1 1 1 2 0 0
'''
N = int(input())
arr = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i] and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

print(' '.join(map(str, result)))