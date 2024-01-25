# 직각삼각형

while True :
    nums= list(map(int, input().split()))
    if sum(nums) == 0 :
        break
    Z = max(nums)
    nums.remove(Z)

    if nums[0] ** 2 + nums[1] ** 2 == Z ** 2 :
        print("right")
    else :
        print('wrong')



