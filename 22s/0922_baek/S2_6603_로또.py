'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''
def func(cnt, start, S, result):    # cnt : 선택개수,  i : 고르기 시작할 개수, S : 들어갈 리스트,
    if cnt == 6:
        print(*result)
        return

    else:
        for i in range(start, len(S)):
            if S[i] not in result :
                result.append(S[i])
                func(cnt+1, i+1, S, result)
                result.pop()

while True:
    data = list(map(int, input().split()))
    K = data[0]     # 총 몇개를 고를지
    S = data[1:]    # 숫자
    result = []


    if K != 0 :                 # 0이 입력되면 종료
        func(0, 0, S, result)
        print()
    else :
        break