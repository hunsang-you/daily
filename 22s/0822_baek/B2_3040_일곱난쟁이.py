arr = [int(input()) for _ in range(9)]

arr2 = [0 for _ in range(9)]
breaker = False

for i in range(9):
    arr2[i] = sum(arr) - arr[i] # i번 째 인덱스에 해당하는 값을 제외한 합
    for j in range(i+1, 9):
        if arr2[i] - arr[j] == 100: # arr2[i]에서 숫자 하나를 뺀 값이 100이면 정답
            a, b = arr[i], arr[j]
            arr.remove(a)
            arr.remove(b)
            breaker = True
            break
    if breaker == True:
        break

for i in range(7):
    print(arr[i])
