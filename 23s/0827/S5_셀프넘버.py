number = list(range(1, 10001))
no = []

for i in number:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        no.append(i)

for no_num in set(no):
    number.remove(no_num)

for self_num in number:
    print(self_num)