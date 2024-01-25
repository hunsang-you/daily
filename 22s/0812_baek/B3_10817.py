# 세 수
A, B, C = map(int, input().split())

lst = []

lst.append(A)
lst.append(B)
lst.append(C)

lst.remove(max(lst))
lst.remove(min(lst))
print(*lst)