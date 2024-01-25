while True :
    num = input()

    ans = "no"
    if num == "0" :
        break

    elif num == num[::-1]:
        ans = "yes"

    print(ans)