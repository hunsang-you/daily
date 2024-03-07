'''
15
'''
# 수학, 브루트포스, 사칙연산
# A ** 2 == B**2 + N
N = int(input())
answer = 0
for i in range(N):
    if i ** 2 > (i-1) ** 2 + N:
        break
    for j in range(1, i+1):
        if i ** 2 == j ** 2 + N:
            answer += 1

print(answer)