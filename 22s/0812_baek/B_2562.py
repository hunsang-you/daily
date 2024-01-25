# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
lst = []

for i in range(9):
    lst.append(int(input()))

for i in range(len(lst) - 1, 0, -1):
    for j in range(0, i):       # 1 ~ 10
        if lst[j] > lst[j + 1] :
            lst[j], lst[j+1] = lst[j+1], lst[j]


print(max(lst))
print(len(lst) -1)

# ===============================

num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)) + 1)