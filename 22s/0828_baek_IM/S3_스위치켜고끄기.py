N = int(input())
switch = list(map(int, input().split()))

student_num = int(input())


for _ in range(student_num):
    gender, button = map(int, input().split())

    if gender == 1:     # 남자 라면
        for i in range(1, (N // button) +1):
            if switch[(button * i) -1] == 0:
                switch[(button * i) - 1] = 1

            elif switch[(button * i) - 1] == 1 :
                switch[(button * i) - 1] = 0


    if gender == 2:
        if switch[(button-1)] == 0:
            switch[(button-1)] = 1

        else :
            switch[(button-1)] = 0

        l = button - 2
        r = button

        while l >= 0 and r < N and switch[l] == switch[r]:
            if switch[l] == 0 :
                switch[l], switch[r] = 1, 1

            else :
                switch[l], switch[r] = 0, 0

            l -= 1
            r += 1

            if l < 0 or r >= N :
                break


    cnt = 0
    answer = ''
    for i in range(N):
        answer += (str(switch[i]) + ' ')
        cnt += 1
        if cnt == 20:
            print(answer)
            answer = ''
            cnt = 0
    if len(answer) != 0:
        print(answer)
