'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
'''

while True:
    lst = input()
    if lst == '.':
        break

    stack = []
    result = True

    for i in lst:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if len(stack)==0 and result == True:
        print('yes')
    else:
        print('no')