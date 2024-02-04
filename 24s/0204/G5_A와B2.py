'''
A
BABA

BAAAAABAA
BAABAAAAAB

A
ABBA
'''
# 브루트포스 재귀

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
ans = 0
def Check(words):
    global ans
    if len(words) == len(S):
        if words == S:
            ans = 1
            return

    else:
        if words[-1] == 'A':
            words.pop()
            Check(words)
            words.append('A')

        if words[0] == 'B':
            words.reverse()
            words.pop()
            Check(words)
            words.append('B')
            words.reverse()

Check(T)
print(ans)