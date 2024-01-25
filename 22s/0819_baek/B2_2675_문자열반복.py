T = int(input())

for test_case in range(1, T+1):
    R, S = input().split()

    for i in S :
        print(int(R) * i, end ='')
    print()
