'''
16 2
1 1
0 1
1 1
0 2
1 2
0 2
0 3
1 3
1 4
1 3
1 3
0 6
1 5
0 5
1 5
1 6

3 3
0 3
1 5
0 6
'''

N, K = map(int, input().split())
male = [0] * 7
female = [0] * 7

for i in range(N):
    gender, grade = map(int, input().split())
    if gender == 0 :            # 여학생인 경우
        female[grade] += 1      # 학년당 학생 += 1

    else :
        male[grade] += 1

# print(male)
# print(female)

room_cnt = 0

for i in range(1, 7):   # 1학년 ~ 6학년 까지 학생수를 보면서 방개수 추가
    # 남학생 분류
    if male[i] % K == 0:
        room_cnt += male[i] // K
        
    elif male[i] % K != 0 :
        room_cnt += male[i] // K + 1
    
    # 여학생 분류
    if female[i] % K == 0 :
        room_cnt += female[i] // K
    
    elif female[i] % K != 0:
        room_cnt += female[i] // K + 1


print(room_cnt)