'''
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
'''
import sys

from collections import deque
N = int(input())
queue = deque()
for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push_front':
        queue.appendleft(order[1])

    elif order[0] == 'push_back':
        queue.append(order[1])

    elif order[0] == 'pop_front':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)

    elif order[0] == 'pop_back':
        if queue:
            print(queue[-1])
            queue.pop()

        else:
            print(-1)

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':
        if queue:
            print(0)
        else :
            print(1)

    elif order[0] == 'front':
        if queue:
            print(queue[0])

        else:
            print(-1)

    elif order[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)