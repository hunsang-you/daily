string = []

while True:
    try:
        string = input()
    except:
        break

    low, upp, num, space = 0, 0, 0, 0

    for i in string:
        if (i.islower()):
            low += 1
        elif (i.isupper()):
            upp += 1
        elif (i.isdigit()):
            num += 1
        elif (i == " "):
            space += 1
    print(low, upp, num, space)