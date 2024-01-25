'''
7 3
'''
N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]
result = []

idx = 0
while len(nums) != 0 :
    idx += (K-1)        # K-1 번째 인덱스의 번호를 뺄 것
    if idx >= len(nums) :        # 만약 그 idx가 남은 숫자의 수보다 크다면
        idx %= len(nums)        # idx % len(nums)로 숫자의 수보다 작게 idx를 바꿔준다.

    result.append(str(nums[idx]))    # 뺸 숫자를 빈 리스트에 추가, 기존 리스트에서 idx번째 인덱스 삭제
    nums.pop(idx)


print('<', ', '.join(result), '>', sep="")
