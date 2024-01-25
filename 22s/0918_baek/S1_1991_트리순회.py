'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
import sys
def preorder(P):        # 선위 순회
    if P != '.':            # 노드가 .이 아니라면
        print(P, end='')
        preorder(tree[P][0])
        preorder(tree[P][1])

def inorder(P):     # 중위 순회
    if P != '.':
        inorder(tree[P][0])
        print(P, end='')
        inorder(tree[P][1])

def postorder(P):   # 후위 순회
    if P != '.':
        postorder(tree[P][0])
        postorder(tree[P][1])
        print(P, end='')

N = int(input())
tree = {}
for _ in range(N):
    P, L, R = input().split()
    tree[P] = [L, R]



preorder('A')
print()
inorder('A')
print()
postorder('A')