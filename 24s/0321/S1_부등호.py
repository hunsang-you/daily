'''
2
< >

9
> < < < > > > < <

'''
# 브루트포스, 백트래킹

import sys
input = sys.stdin.readline

K = int(input())

arr = list(map(str, input().rstrip().split()))
visited = [0] * 10
ans = []

# 완성된 식이 부등호가 맞는지 아닌지 확인
def check(num1, num2, oper):
    if oper == '<':
        if num1 > num2 :
            return False

    if oper == '>':
        if num1 < num2 :
            return False
    return True

def DFS(num, cnt):
    # cnt가 부등호+1 만큼 들어왔으면 리턴
    if cnt == K+1:
        ans.append(num)
        return

    for i in range(10):
        # 이미 사용한 숫자면 넘어감
        if visited[i] == 1:
            continue

        if cnt == 0 or check(num[cnt-1], str(i), arr[cnt-1]):
            visited[i] = 1
            DFS(num + str(i), cnt+1)
            visited[i] = 0



DFS('', 0)
print(max(ans), min(ans), sep='\n')