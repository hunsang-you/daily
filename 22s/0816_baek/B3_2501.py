# 약수 구하기

N, K = map(int, input().split())
num = []
cnt = 0

for i in range(1, N+1):
    if N % i == 0 :
        num.append(i)
    cnt += 1

if len(num) < K :
    print("0")

else :
    print(num[K-1])



