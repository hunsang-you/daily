'''
1 10

15 15

1 1000
'''
# 에라토스테네스의 체
# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다.
# min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

import sys
input = sys.stdin.readline

minNum, maxNum = map(int, input().split())
check = [False] * (maxNum-minNum+1)
answer = maxNum - minNum + 1
for i in range(2, int(maxNum ** 0.5+1)):
    square = i ** 2
    for j in range((((minNum-1) // square)+1)* square, maxNum+1, square):
        if check[j-minNum] == 0:
            check[j-minNum] = True
            answer -= 1
print(answer)
