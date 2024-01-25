# 상수
A, B = input().split()

num1 = int(A[::-1])
num2 = int(B[::-1])

if num1 > num2 :
    print(num1)

else :
    print(num2)