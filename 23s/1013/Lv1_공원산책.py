'''
park	                    routes      	result
["SOO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]
'''

def solution(park, routes):

    x = 0
    y = 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break

    for route in routes:
        nx = x
        ny = y

        for go in range(int(route[2])):
            # 동쪽
            if route[0] == 'E' and nx != len(park[0])-1 and park[ny][nx+1] != 'X':
                nx += 1
                if go == int(route[2]) - 1:
                    x = nx

            # 서쪽
            elif route[0] == 'W' and nx != 0 and park[ny][nx-1] != 'X':
                nx -= 1
                if go == int(route[2]) - 1:
                    x = nx

            # 북쪽
            elif route[0] == 'N' and ny != 0 and park[ny-1][nx] != 'X':
                ny -= 1
                if go == int(route[2]) - 1:
                    y = ny

            # 남쪽
            elif route[0] == 'S' and ny != len(park[0])-1 and park[ny+1][nx] != 'X':
                ny += 1
                if go == int(route[2]) - 1:
                    y = ny

    return [y, x]

solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])