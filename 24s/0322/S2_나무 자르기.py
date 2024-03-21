'''
5
1 3 2 4 6
2 7 3 4 1

'''
# 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
# [현재길이, 자라는 길이]
tree = [[] for _ in range(N)]
for i in range(N):
    tree[i] = [H[i], A[i]]

# 자라는 길이 오름차순 정렬
tree.sort(key=lambda x:x[1])

# 가장 오래 자랐을때, 최대한으로 자르기
for i in range(N):
    ans += tree[i][0] + i * (tree[i][1])

print(ans)
