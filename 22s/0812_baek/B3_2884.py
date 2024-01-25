# 알람시계
H, M = map(int, input().split())

if M < 45 :
    H = H - 1
    M = M + 15
    if H < 0 :
        H = 23
else :
    H = H
    M = M - 45

print(H, M)

