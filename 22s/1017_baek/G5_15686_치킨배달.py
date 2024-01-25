'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
distance = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])

        elif board[i][j] == 2:
            chicken.append([i, j])


for x1, y1 in house:
    for x2, y2 in chicken:
        distance.append((abs(x1-x2) + abs(y1- y2)))

for i in range(0, len(distance), len(chicken)):



print(house)
print(chicken)
print(distance)