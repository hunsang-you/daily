'''
6 3 2 2

2 2 1 1
'''
# 그리디, 시뮬레이션

N, K, A, B = map(int, input().split())

arr = [K] * N
answer = 0
# 수분의 양이 0이 아닐동안 반복
while min(arr) != 0:
    # 수분이 적은 순서대로 정렬
    arr.sort()

    # 가장 수분의 양이 적은 화분이 존재하는 곳에 물을 준다
    for i in range(A):
        arr[i] += B

    # 매일 수분이 1씩 감소
    for i in range(N):
        arr[i] -= 1

    answer += 1

print(answer)