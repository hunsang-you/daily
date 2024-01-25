'''
A	        B	        answer
[1, 4, 2]	[5, 4, 4]	29
[1,2]	    [3,4]	    10
'''
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다.
# 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)
def solution(A,B):
    ans = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        ans += (A[i] * B[i])
    return ans
solution([1, 4, 2], [5, 4, 4])