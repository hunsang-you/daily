'''
3
NYY
YNY
YYN

3
NNN
NNN
NNN

5
NYNNN
YNYNN
NYNYN
NNYNY
NNNYN

10
NNNNYNNNNN
NNNNYNYYNN
NNNYYYNNNN
NNYNNNNNNN
YYYNNNNNNY
NNYNNNNNYN
NYNNNNNYNN
NYNNNNYNNN
NNNNNYNNNN
NNNNYNNNNN

15
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNYNNNNNNN
NNNNNNNYNNNNNNY
NNNNNNNNNNNNNNY
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNYYNNNNNNNNNNN
NNNNNYNNNNNYNNN
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
YNNYYNNNNYNNNNN
'''
# 그래프 이론, 플로이드-워셜, 브루트포스
import sys
input = sys.stdin.readline
N = int(input())

line = [[0] * N for _ in range(N)]
graph = [list(input().rstrip()) for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                line[i][j] = 1

answer = 0

for i in line:
    answer = max(answer, sum(i))
print(answer)