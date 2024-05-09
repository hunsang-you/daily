'''
1
13
OOIOIOIOIIOII

2
13
OOIOIOIOIIOII

'''
# 문자열

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

P = 'I' + ('OI' * N)
ans = 0
idx = 0
cnt = 0

while idx < M-1:
    if S[idx: idx + 3] == 'IOI':
        idx += 2
        cnt += 1

        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(ans)