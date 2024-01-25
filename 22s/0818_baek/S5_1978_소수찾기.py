# 소수찾기
N = int(input()) # 입력받을 숫자의 개수
numbers = list(map(int, input().split()))
prime = []          # 소수 리스트


for num in numbers:
    div = 0                 # 나눠지는 횟수
    if num == 1:           # 1은 소수가 아니기 때문에 건너띔
        div = 1
    if num != 1 :
        for i in range(2, num+1):           # 2 ~ num까지의 숫자들 중 나눠지는 수가 있으면 안된다.
            if num % i == 0:
                div += 1                    # 나눠지는 횟수 증가

        if div == 1:                        # 약수가 1을 제외하고 자기 자신밖에 없는 경우
            prime.append(num)

    print(div+1)                        # 본인을 포함한 약수의 수



print(len(prime))                      # 입력된 숫자들 중 소수의 갯수