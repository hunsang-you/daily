'''
4
DOG
GOD
GOOD
DOLL
'''

import sys
input = sys.stdin.readline

N = int(input())
word = list(input().rstrip())
answer = 0

for _ in range(N-1):
    alp = word[:]
    new = list(input().rstrip())
    cnt = 0

    for i in new:
        if i in alp:
            alp.remove(i)

        else:
            cnt += 1
    if cnt < 2 and len(alp) < 2 :
        answer += 1

print(answer)