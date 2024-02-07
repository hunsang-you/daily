'''
57 2
'''

A, P = map(int, input().split())

numbers = [A]

while True:
    next = 0
    for i in list(str(numbers[-1])):
        next += int(i) ** P

    if next in numbers:
        break
    else:
        numbers.append(next)

print(numbers.index(next))
