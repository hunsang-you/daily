color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

R1 = color.index(input())
R2 = color.index(input())
R3 = color.index(input())

print(int(str(R1) + str(R2)) * (10 ** R3))