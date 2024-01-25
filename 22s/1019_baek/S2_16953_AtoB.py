'''
2 162
4 42
100 40021
'''

A, B = map(int, input().split())
cnt = 1

# 끝에 1이 있으면 1부터 없애는게 최소한의 방법
while True:        # B -> A 로 거꾸로 가는 방법
    if A == B:
        break

    elif (A > B) or (B % 10 != 1 and B % 2 != 0) :        # A가 B보다 커지거나, 두 조건이 불가능하면 방법이 없으므로 -1을 출력
        cnt = -1
        break


    else:
        if B % 10 == 1 :        # B를 10으로 나누었을때 나머지가 1이면 끝자리가 1이므로 1을 없애준다
            B //= 10
            cnt += 1
        else:          # 끝이 1이 아니라면 2로 나눈다
            B //= 2
            cnt += 1



print(cnt)
