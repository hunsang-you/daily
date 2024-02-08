'''
baekjoon online judge

<open>tag<close>

<ab cd>ef gh<ij kl>

one1 two2 three3 4fourr 5five 6six

<int><max>2147483647<long long><max>9223372036854775807

<problem>31471<is hardest>melborp reve<end>
'''

import sys
input = sys.stdin.readline

words = list(input().rstrip() + ' ')
stack = []

result = ""
check = False

for i in words:
    if i == '<':
        check = True

        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == '>' and check == True:
        check = False

        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == ' ' and check == False:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

print(result)