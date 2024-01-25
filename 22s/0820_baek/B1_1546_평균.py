N = int(input())

M = list(map(int, input().split()))

new_score = []

for i in range(N):
    score = M[i] / max(M) * 100
    new_score.append(score)

avg = sum(new_score) / len(new_score)

print(avg)