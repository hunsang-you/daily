'''
n	result
15	4
'''
def solution(n):
    answer = 0
    # dp = [0] * n
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n :
                answer += 1
                break

            if temp > n:
                break
    return (answer)

solution(15)