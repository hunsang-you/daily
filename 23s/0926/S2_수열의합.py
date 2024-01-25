'''
18 2

18 4

18 5

45 10

1000000000 2
'''
# N, L 이 주어질 때, 합이 N이면서 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트
import sys
input = sys.stdin.readline
N, L = map(int, input().split())

# 18 = 5 + 6 + 7
# 18 = 3 + 4 + 5 + 6
# (x+1) + (x+2) + (x+3) + ... + (x+i) = i/2 * (x+1+x+i) = ix + i / 2 * (i+1) = N
# ix로 정리하면 ix = N - i(i+1)/2
# i = 숫자의 갯수, 우변은 정수임이 보장
# => x가 정수 and x+1 > 0

for i in range(L, 101):
    ix = N - (i *(i+1) // 2)

    if ix % i == 0:
        x = ix // i
        if x + 1 >= 0:
            print(*(i for i in range(x+1, x+i+1)))
            break

else:
    print(-1)