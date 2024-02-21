'''
20 1
HHPHPPHHPPHPPPHPHPHP

20 2
HHHHHPPPPPHPHPHPHHHP
'''
# 그리디
# P(사람), H(햄버거)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = list(input().rstrip())
answer = 0
for i in range(N):
    if table[i] == 'P':
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if table[j] == 'H':
                table[j] = 1
                answer += 1
                break

print(answer)