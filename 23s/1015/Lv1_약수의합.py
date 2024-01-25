def solution(n):
    temp = n
    if n == 0:
        temp = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            temp += i

    return temp
solution(12)