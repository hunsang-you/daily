'''
110
1
210
1000
500
'''

N = int(input())

answer = 0

for i in range(1, N+1):
    N_lst = list(map(int, str(i)))

    if i  < 100 :
        answer += 1     # 100보다 작으면 모두 한수가 된다.

    elif N_lst[0] - N_lst[1] == N_lst[1] - N_lst[2] :
        answer += 1     # 1, 2번째 자리의 차와 2, 3번째 자리의 차가 같으면 한수

print(answer)