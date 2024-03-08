'''
매개변수	                                                                    값
n	                                                                        5
arr1	                                                                    [9, 20, 28, 18, 11]
arr2	                                                                    [30, 1, 21, 17, 28]

출력
["#####","# # #", "### #", "# ##", "#####"]


n	                                                                        6
arr1	                                                                    [46, 33, 33 ,22, 31, 50]
arr2	                                                                    [27 ,56, 19, 14, 14, 10]

출력
["######", "### #", "## ##", " #### ", " #####", "### # "]
'''

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
def solution(n, arr1, arr2):
    answer = []
    board1 = []
    board2 = []
    for i in range(n):
        board1.append(bin(arr1[i])[2:])
        board2.append(bin(arr2[i])[2:])
        board1[i] = ('0' * (n - len(board1[i]))) + board1[i]
        board2[i] = ('0' * (n - len(board2[i]))) + board2[i]

        temp = ''
        for j in range(n):
            if board1[i][j] == '1' or board2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

solution(n, arr1, arr2)