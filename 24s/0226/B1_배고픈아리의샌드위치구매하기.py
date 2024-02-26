'''
1023 12

1024 1

1024 2
'''
# 수학, 비트마스킹

S, M = map(int, input().split())
coin = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

if S < 1024:
    print('No thanks')

else:
    temp = S - 1023

    if (temp & M) == temp:
        print('Thanks')
    else:
        print("Impossible")

