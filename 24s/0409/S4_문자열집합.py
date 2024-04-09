'''
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

'''
# 자료구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {}
for _ in range(N):
    word = input().rstrip()
    S[word] = 1

ans = 0
for _ in range(M):
    word = input().rstrip()
    if word in S:
        ans += 1

print(ans)