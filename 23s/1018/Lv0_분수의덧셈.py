
numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4

answer = []
answer.append(numer1 * denom2 + numer2 * denom1)
answer.append(denom1 * denom2)
for i in range(answer[1] + 1, 1, -1):
    print(i)
    if answer[0] % i == 0 and answer[1] % i == 0:
        answer[0] = answer[0] // i
        answer[1] = answer[1] // i
    print(answer)