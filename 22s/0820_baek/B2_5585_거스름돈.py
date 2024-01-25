# 거스름돈

N = int(input())
charge = 1000 - N


cnt = 0
while charge > 0 :
    if charge >= 500 :
        charge -= 500
        cnt += 1

    elif 100 <= charge < 500 :
        charge -= 100
        cnt += 1

    elif 50 <= charge < 100 :
        charge -= 50
        cnt += 1

    elif 10 <= charge < 50 :
        charge -= 10
        cnt += 1


    elif 5 <= charge < 10:
        charge -= 5
        cnt += 1

    elif 1<= charge < 5 :
        charge -= 1
        cnt += 1

print(cnt)