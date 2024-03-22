'''
sticker	                            answer
[14, 6, 5, 11, 3, 9, 2, 10]	        36
[1, 3, 2, 5, 4]	                    8
'''

# sticker = [14, 6, 5, 11, 3, 9, 2, 10]
sticker = [1, 3, 2, 5, 4]


def solution(sticker):
    N = len(sticker)

    if N == 1:
        return sticker[0]

    # 처음 스티커를 고르는 경우
    DP = [[0 for _ in range(N)] for _ in range(2)]
    DP[0][0], DP[0][1] = sticker[0], sticker[0]
    DP[1][1] = sticker[1]

    # 1번째 것을 고르면
    for i in range(2, N-1):
        DP[0][i] = max(DP[0][i-2]+sticker[i], DP[0][i-1])

    # 2번째 것을 고르는 경우
    for i in range(2, N):
        DP[1][i] = max(DP[1][i-2]+sticker[i], DP[1][i-1])


    answer = max(max(DP[0]), max(DP[1]))




    return answer

solution(sticker)
# print(solution(sticker))
