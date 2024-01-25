'''
5
-1 0 0 1 1
2

5
-1 0 0 1 1
1

5
-1 0 0 1 1
0

9
-1 0 0 2 2 4 4 6 6
4
'''

import sys
input = sys.stdin.readline


def DFS(num, dot):
    dot[num] = -2
    for i in range(len(dot)):
        if num == dot[i]:
            DFS(i, dot)


N = int(input())
dot = list(map(int, input().split()))
K = int(input())

DFS(K, dot)
cnt = 0

for i in range(len(dot)):
    if dot[i] != -2 and i not in dot:
        cnt += 1

print(cnt)