from collections import deque
N = int(input())
Queue = deque()

for i in range(1, N+1):
    Queue.append(i)

while len(Queue):
    Queue.popleft()
    Queue.append(Queue.popleft())

print(Queue[0])