# readline을 사용안하면 시간초과 ///  메모리 초과 // 8MB로 제한되어 있어 sort를 사용하면 메모리초과가 일어난다
# import sys
# N = int(input())
#
# number = []
# for i in range(N):
#     num = int(sys.stdin.readline())
#     number.append(num)
# number = sorted(number)
#
# for i in range(len(number)):
#     print(number[i])


import sys
N = int(input())

number = [0] * 1001


for i in range(N):
    num = int(sys.stdin.readline())
    number[num] = number[num] + 1

for i in range(1001):
    if number[i] != 0:
        for j in range(number[i]):
            print(i)

