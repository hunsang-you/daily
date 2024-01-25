# 네번쨰 점

x_coor = []
y_coor = []

for i in range(3):
    x, y = map(int, input().split())
    x_coor.append(x)
    y_coor.append(y)

for j in range(3):
    if x_coor.count(x_coor[j]) == 1:
        x_num = x_coor[j]

    if y_coor.count(y_coor[j]) == 1:
        y_num = y_coor[j]

print(x_num, y_num)