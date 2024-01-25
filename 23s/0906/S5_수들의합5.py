'''
15
'''

N = int(input())

cnt = 1
start, end = 1, 1
temp = 1

while end != N:

    if temp == N :
        cnt += 1
        end += 1
        temp += end

    elif temp > N:
        temp -= start
        start += 1

    else :
        end += 1
        temp += end

print(cnt)