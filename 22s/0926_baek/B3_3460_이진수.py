'''
1
13
'''

T = int(input())

for test_case in range(T):
    n = int(input())

    result = []
    cnt = 0

    while n > 0 :
        if n % 2 :
            result.append(cnt)

        n //= 2
        cnt += 1
    print(' '.join(map(str, result)))
