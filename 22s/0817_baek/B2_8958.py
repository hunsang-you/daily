# OX퀴즈
T = int(input())

for test_case in range(T):
    ox = list(input())
    score = 0               # 연속된 O가 나올때 추가해줄 점수
    tot_score = 0           # 총 점수

    for i in ox:
        if i == 'O' :
            score += 1
            tot_score += score

        else :              # i가 X라면
            score = 0

    print(tot_score)
