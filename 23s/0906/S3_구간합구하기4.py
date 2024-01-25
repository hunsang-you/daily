'''
5 3
5 4 3 2 1
1 3
2 4
5 5
'''
import sys
N, M = map(int, sys.stdin.readline().split())
Narr = list(map(int, sys.stdin.readline().split()))
arrSum = [0]
temp = 0
for i in Narr:
    temp += i
    arrSum.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(arrSum[j]-arrSum[i-1])