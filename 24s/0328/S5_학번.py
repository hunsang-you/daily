'''
2
1
124866
3
124866
111111
987651

'''
# 수학, 브루트포스, 정수론

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    G = int(input())
    students = [int(input()) for _ in range(G)]
    if G == 1:
        print(1)
    else:
        number = 2
        while True:
            lst = []
            for i in range(G):
                lst.append(students[i] % number)

            ans = list(set(lst))
            if G == len(ans):
                print(number)
                break
            else:
                number += 1

