# ★ : 4 ,● : 3, ■ : 2, ▲ : 1

round = int(input())


for _ in range(round):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
    B_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0}


    # A, B가 내는 모양의 갯수를 dict에 count하기
    # A
    for i in range(1, len(A)):
        if A[i] in A_dict :
            A_dict[A[i]] += 1

    for i in range(1, len(B)):
        if B[i] in B_dict :
            B_dict[B[i]] += 1

    A_lst = list(A_dict.values())
    B_lst = list(B_dict.values())


    if A_lst[3] != B_lst[3] :
        if A_lst[3] > B_lst[3] :
            print('A')
        elif A_lst[3] < B_lst[3] :
            print('B')


    elif A_lst[2] != B_lst[2] :
        if A_lst[2] > B_lst[2] :
            print('A')
        elif A_lst[2] < B_lst[2] :
            print('B')

    elif A_lst[1] != B_lst[1] :
        if A_lst[1] > B_lst[1] :
            print('A')
        elif A_lst[1] < B_lst[1] :
            print('B')

    elif A_lst[0] != B_lst[0] :
        if A_lst[0] > B_lst[0] :
            print('A')
        elif A_lst[0] < B_lst[0] :
            print('B')
    else :
        print('D')



# print('A :', A_lst)
# print('B :', B_lst)
# print()