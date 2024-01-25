A, B = map(int, input().split())

lst = []
for i in range(1, min(A,B) + 1):
    if A % i == 0 and B % i == 0 :
        lst.append(i)

GCD = max(lst)         # 최대공약수

LCM = A * B // GCD      # 최소공배수

print(GCD)
print(LCM)