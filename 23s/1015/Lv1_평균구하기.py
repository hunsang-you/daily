'''
arr	            return
[1,2,3,4]	    2.5
[5,5]	        5
'''
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
def solution(arr):
    temp = 0
    for i in arr:
        temp += i
    temp = temp // len(arr)
    return temp


solution([1,2,3,4])