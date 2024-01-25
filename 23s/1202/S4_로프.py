'''
2
10
15
'''
# 그리디


N = int(input())
weights = [int(input()) for _ in range(N)]

weights.sort()

answer = []

for weight in weights:
    answer.append(weight * N)
    N -= 1

print(max(answer))