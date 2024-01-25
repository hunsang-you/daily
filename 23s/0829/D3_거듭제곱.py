'''
1
9 8
2
2 8
'''




for _ in range(10):
    T = int(input())
    x, y = map(int, input().split())

    print(f"#{T} {x ** y}")