'''
land	                                    answer
[[1,2,3,5],[5,6,7,8],[4,3,2,1]]             	16


'''
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):

    N = len(land)

    for i in range(1, N):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    answer = max(land[N-1])
    return answer

solution(land)
