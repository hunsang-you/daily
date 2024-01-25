'''
3
ABAB
AABB
ABBA
3
AAA
AA
AB
1
ABBABB
'''
N = int(input())
cnt = 0

for _ in range(N):
    words = input()
    stack = []

    for alp in words:
        if len(stack) == 0 :
            stack.append(alp)

        else:
            if alp == 'A':
                if stack[-1] == 'A':
                    stack.pop()
                else :
                    stack.append(alp)

            else :
                if stack[-1] == 'A':
                    stack.append(alp)

                else :
                    stack.pop()
    if len(stack) == 0:
        cnt += 1

print(cnt)