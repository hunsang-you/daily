'''
4 6
a t c i s w
'''
# 브루트포스, 백트래킹
# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
# 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

def func(pw):
    v_count, c_count = 0, 0

    for i in pw:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True

    else:
        return False

def backtracking(pw):
    if len(pw) == L:
        if func(pw):
            print("".join(pw))
            return

    for i in range(len(pw), C):
        if pw[-1] < arr[i]:
            pw.append(arr[i])
            backtracking(pw)
            pw.pop()

for i in range(C-L+1):
    a = [arr[i]]
    backtracking(a)