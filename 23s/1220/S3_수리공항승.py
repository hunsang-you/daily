'''
4 2
1 2 100 101

4 3
1 2 3 4

3 1
3 2 1
'''
# 그리디, 정렬

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pipe = list(map(int, input().split()))

pipe.sort()

start = pipe[0]
cnt = 1

for rep in pipe:
    if rep in range(start, start+L):
        continue
    else:
        start = rep
        cnt += 1
print(cnt)