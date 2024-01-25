'''
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
'''
import sys

N, M = map(int, input().split())
lst1 = [0] * N
lst2 = [0] * M


for i in range(N):
    lst1[i] = sys.stdin.readline()

for i in range(M):
    lst2[i] = sys.stdin.readline()

cnt = 0
result = []
for i in range(N):
    for j in range(M):
        if lst1[i] == lst2[j] :
            result.append(lst1[i])
            cnt += 1


print(cnt)
for i in range(len(result)):
    print(result[i])

