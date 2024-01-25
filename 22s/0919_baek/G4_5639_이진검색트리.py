'''
50
30
24
5
28
45
98
52
60
'''
import sys
sys.setrecursionlimit(1000000)

def func(start, end):
    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return
    temp = end + 1

    # 서브트리 찾기
    for i in range(start + 1, end +1):
        if graph[start] < graph[i]:
            temp = i
            break
    func(start+1, temp-1)        # 왼쪽 서브 트리 탐색
    func(temp, end)     # 오른쪽 서브트리 탐색
    print(graph[start])

# 입력이 없을 때까지 반복하여 입력을 리스트에 추가
graph = []
while True:
    try:
        graph.append(int(input()))

    except:
        break

func(0, len(graph)-1)