# 영수증

tot_price = int(input())

for i in range(9):
    price = int(input())
    tot_price -= price

print(tot_price)