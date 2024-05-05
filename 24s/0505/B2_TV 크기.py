'''
52 9 16

7 2 3

13 7 10

7 32 47

11 15 16

'''
# 기하학, 피타고라스 정리

D, H, W = map(int, input().split())

r = D/(H ** 2 + W ** 2) ** 0.5
print(int(H * r), int(W * r))
