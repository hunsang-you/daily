# 숫자의 갯수
A = int(input())
B = int(input())
C = int(input())

D = list(str(A * B * C))

dic = {}

for i in range(10):
    print(D.count(str(i)))
