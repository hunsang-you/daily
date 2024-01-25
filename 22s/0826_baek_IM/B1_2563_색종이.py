'''
3
3 7
15 7
5 2
'''

board = [[0] * 100 for _ in range(100)]

N = int(input())


sumV = 0
for i in range(N):
    x, y = map(int,input().split())
    for k in range(y, y+10):
        for l in range(x, x+10):
            board[k][l] = 1

for i in range(100):
    for j in range(100):
        sumV += board[i][j]

print(sumV)
