'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()
'''

T = int(input())
for _ in range(T):
    lst = list(input())
    check = 0
    result = 'YES'

    for i in lst:
        if i == '(':
            check += 1
        elif i == ')':
            check -= 1

        if check < 0:
            result = 'NO'
            print(result)
            break

    if check > 0:
        result = 'NO'
        print(result)
    elif check == 0:
        print(result)