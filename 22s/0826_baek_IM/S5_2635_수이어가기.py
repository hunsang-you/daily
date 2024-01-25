N = int(input())
i = int(input())
result = []

for _ in range(1, N+1):
    first = N
    second = i
    temp = [N, i]
    while True:
        next = first - second
        if next >= 0 :           # 0 이상일때
            result.append(next)
            first, second = second, next

        else :                  # 음수가 나올때 멈춘다
            if len(temp) > len(result):
                result = temp
            break


print(result)