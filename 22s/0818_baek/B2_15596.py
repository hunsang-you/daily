# 정수 N개의 합(함수구현)

def solve(a):

    ans = 0

    for i in a:
        ans += i

    return ans


print(solve([1, 5, 1, 2]))