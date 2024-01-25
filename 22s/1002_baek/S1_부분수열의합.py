'''
3
5 1 2
3
2 1 4
4
2 1 2 7
'''
def backtrack(k, res):
    if k >= N:
        return lst
    else:
        res += S[k]
        lst[res] = 1
        backtrack(k+1, res - S[k])
        backtrack(k+1, res)
N = int(input())
S = list(map(int, input().split()))

lst = [0] * 2000000
backtrack(0, 0)
for i in range(1, len(lst)):
    if lst[i] == 0:
        print(i)
        break

# =======
S.sort()

num = 1
for i in S:
    if num < i:
        break
    num += i
print(num)