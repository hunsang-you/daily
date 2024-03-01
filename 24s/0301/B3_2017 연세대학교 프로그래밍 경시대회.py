'''
6

'''
# 브루트포스, 사칙연산

N = int(input())
answer = 0
for i in range(2, N-1, 2):
    answer += (N-i-2)//2
print(answer)
