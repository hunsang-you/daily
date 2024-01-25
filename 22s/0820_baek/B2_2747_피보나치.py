# 피보나치
# def fibo(N):
#     if N == 0 :
#         return 0
#
#     elif N < 2 :
#         return 1
#
#     else :
#         return fibo(N-1) + fibo(N-2)
#
#
# N = int(input())
# print(fibo(N))

N = int(input())

a, b = 0, 1

for i in range(N):
    a, b = b, a+b

print(a)