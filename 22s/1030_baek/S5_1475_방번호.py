'''
9999
122
12635
888888
'''
N = input()
nums = [0] * 10

for i in range(len(N)):
    num = int(N[i])
    nums[num] += 1

    # num이 6이거나 9라면 서로 바꿔서 사용할 수 있다.
    if nums[6] < nums[9] :       # 6이 나온 횟수보다 9가 나온 횟수가 더 많다면 9횟수만큼 6으로 옮긴다
        nums[9] -= 1
        nums[6] += 1

    elif nums[6] > nums[9] :
        nums[6] -= 1
        nums[9] += 1

print(max(nums))