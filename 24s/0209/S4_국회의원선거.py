'''
3
5
7
7

4
10
10
10
10

1
1

5
5
10
7
3
8
'''
# 구현, 그리디, 우선순위 큐

N = int(input())
me = int(input())
others = [int(input()) for _ in range(N-1)]
answer = 0

if N == 1:
    print(answer)

else:
    others.sort(reverse=True)
    while others[0] >= me:
        me += 1
        others[0] -= 1
        answer += 1
        others.sort(reverse=True)

    print(answer)