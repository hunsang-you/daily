'''
10 3
1 2 3
10 3
2 9 5
32 6
27 16 30 11 6 23
'''

from collections import deque

N, M = map(int, input().split())        # N : 큐의 크기, M : 뽑아내려는 수의 갯수
target = list(map(int, input().split()))        # 뽑아내려는 수
queue = deque([i for i in range(1, N+1)])


cnt = 0     # 2, 3번째 연산을 하면 추가
for i in range(len(target)):
    while True:
        if queue[0] == target[i] :
            queue.popleft()
            break

        else:
            if queue.index(target[i]) < len(queue)/ 2:         # target의 숫자가 queue의 좌편향되어있으면 왼쪽으로 움직임
                while queue[0] != target[i]:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != target[i]:
                    queue.appendleft(queue.pop())
                    cnt += 1


print(cnt)