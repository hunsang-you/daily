'''
10
20
30
40
50
60
70
80
90
100
'''
m = []
score = 0
for i in range(10):
    m.append(int(input()))
for j in m:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)