'''
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###

8 8
.######.
#..o...#
#.####.#
#.#v.#.#
#.#.o#o#
#o.##..#
#.v..v.#
.######.

9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
'''
# 그래프 이론, 탐색, BFS, DFS
# 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

sheep, wolf = 0, 0
def DFS(x, y):
    global a, b
    if 0 <= x < R and 0 <= y < C:
        if board[x][y] != '#' and visited[x][y] == 0:
            visited[x][y] = 1
            if board[x][y] == 'o':
                a += 1

            if board[x][y] == 'v':
                b += 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                DFS(nx, ny)
            return True
        return False

for i in range(R):
    for j in range(C):
        a, b = 0, 0
        if DFS(i, j) == True:
            if a > b:
                sheep += a

            else:
                wolf += b

print(sheep, wolf)
