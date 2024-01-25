'''
1 1
5 5
7 3

1 1
3 3
5 5

1 1
7 3
5 5
'''
# P1, P2, P3를 순서대로 이은 선분이 반시계 방향을 나타내면 1, 시계 방향이면 -1, 일직선이면 0을 출력한다.
def ccw(p1,p2,p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1]))


P = []
for i in range(3):
    x, y = map(int, input().split())
    P.append([x, y])

ans = ccw(P[0],P[1],P[2])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)