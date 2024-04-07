'''
adaabc aababbc

hello xello

koder topcoder

abc topabcoder

giorgi igroig

'''
# 문자열, 브루트포스

import sys
input = sys.stdin.readline

word1, word2 = input().split()
ans = []

for i in range(len(word2) - len(word1) +1):
    cnt = 0
    for j in range(len(word1)):
        if word1[j] != word2[i + j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))