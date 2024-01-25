lst = []
for i in range(7):
    a = int(input())
    if a % 2 != 0:
        lst.append(a)
if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)