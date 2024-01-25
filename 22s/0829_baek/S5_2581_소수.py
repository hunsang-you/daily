# 자연수 M이상 N 이하의 자연수중 소수만 골라 이들의 합과 최솟값을 출력
'''
60
100
64
65
'''
M = int(input())
N = int(input())

prime = []

for i in range(M, N+1):       # M 이상, N이하인 i(비교할수)
    for j in range(2, i+1):           # i가 소수인지 판별할 2부터 자기자신까지인 j

        if i == j :              # i가 j와 같다면 소수
            prime.append(i)
        elif i % j == 0 :             # i가 j로 나누었을떄 나머지가 0이라면 소수가 아니다
            break
if not prime :
    print(-1)
else:
    print(sum(prime))
    print(prime[0])

