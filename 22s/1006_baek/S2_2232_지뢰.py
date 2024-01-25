'''
9
1
2
5
4
3
3
6
6
2
'''
import sys
N = int(input())
bomb = [0]
# cnt = 0             # 터진 횟수 확인
for _ in range(N):
    bomb.append(int(sys.stdin.readline()))
bomb.append(0)
check = [0] * (N+2)         # 폭탄를 직접 터뜨린 곳 체크

for i in range(1, N+1):
    if bomb[i-1] <= bomb[i] and bomb[i] >= bomb[i+1]:   # 양쪽보다 커야만 의미가 있다.
        check[i] = i
        # cnt += 1
# print(cnt)
print(bomb)
print(check)
for i in range(len(check)):
    if check[i] :
        print(check[i])

