'''
1010

000011


S의 길이는 2 이상 500 이하이다.
S는 짝수 개의 0과 짝수 개의 1로 이루어져 있다.

S의 길이는 4의 배수이다.
S의 홀수 번째 문자는 1, 짝수 번째 문자는 0이다.

'''
# 그리디, 문자열

import sys
input = sys.stdin.readline

words = list(input().rstrip())

zero, one = words.count('0') // 2, words.count('1') // 2
s = ''

