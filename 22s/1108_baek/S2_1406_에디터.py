'''
abcd
3
P x
L
P y
abc
9
L
L
L
L
L
P x
L
B
P y
'''
# L D B P$ // L이 나오면 우측에 있는 것을 빈리스트에 추가, D가 나오면 word2에서 빼서 다시 기존리스트에 추가
import sys
word1 = list(input())
word2 = []
M = int(input())
for _ in range(M):
    cursor = list(sys.stdin.readline().split())
    if cursor[0] == 'L':
        if len(word1):
            word2.append(word1.pop())

    elif cursor[0] == 'D':
        if len(word2):          # 새로 만드는 단어길이가 1이상
            word1.append(word2.pop())

    elif cursor[0] == 'B':
        if len(word1):
            word1.pop()

    else :      # cursor[0] == 'P'
        word1.append(cursor[1])

word2.reverse()
print(*word1+word2, sep="")
# print(word1)
# print(word2)
# print(word1+word2)
