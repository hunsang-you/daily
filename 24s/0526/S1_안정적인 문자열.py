'''
}{
{}{}{}
{{{}
---

'''
# 자려구조, 그리디 알고리즘, 문자열, 스택

import sys
input = sys.stdin.readline

num = 1
while True:
    words = input().rstrip()
    if '-' in words:
        break

    stack = []
    cnt = 0

    for i in words:
        if i == '{':
            stack.append(i)

        else:
            if stack:
                stack.pop()

            else:
                cnt += 1
                stack.append('{')

    cnt += len(stack) // 2
    print(f'{num}. {cnt}')
    num += 1

