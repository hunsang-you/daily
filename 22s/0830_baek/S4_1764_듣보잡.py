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

result = sorted(list(set(lst1) & set(lst2)))
cnt = len(result)


print(cnt)
for i in range(len(result)):
    print(result[i], end= '')

