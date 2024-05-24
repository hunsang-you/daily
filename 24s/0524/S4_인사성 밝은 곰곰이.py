'''
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402

9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402

9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402

3
ENTER
lms0806
lms0806

'''
# 자료 구조, 해시를 이용한 집합과 맵, 트리를 사용한 집합과 맵

import sys
input = sys.stdin.readline


N = int(input())

gom = set()

cnt = 0
for i in range(N):
    word = input().rstrip()
    if word != 'ENTER':
        if word not in gom:
            cnt += 1
            gom.add(word)

    elif word == 'ENTER':
        gom.clear()

print(cnt)