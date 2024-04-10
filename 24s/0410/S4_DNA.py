'''
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT

4 10
ACGTACGTAC
CCGTACGTAG
GCGTACGTAT
TCGTACGTAA

6 10
ATGTTACCAT
AAGTTACGAT
AACAAAGCAA
AAGTTACCTT
AAGTTACCAA
TACTTACCAA

'''
# 구현, 그리디, 문자열, 브루트포스

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(str, input().rstrip())) for _ in range(N)]

cnt = 0
word = ''

for i in range(M):
    check = [0, 0, 0, 0]        # A, C, G, T 갯수
    for j in range(N):
        if board[j][i] == 'A':
            check[0] += 1

        elif board[j][i] == 'C':
            check[1] += 1

        elif board[j][i] == 'G':
            check[2] += 1

        elif board[j][i] == 'T':
            check[3] += 1

    idx = check.index(max(check))

    if idx == 0:
        word += 'A'

    elif idx == 1:
        word += 'C'

    elif idx == 2:
        word += 'G'

    elif idx == 3:
        word += 'T'

    cnt += N - max(check)

print(word)
print(cnt)