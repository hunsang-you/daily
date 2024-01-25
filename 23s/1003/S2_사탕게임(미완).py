'''
3
CCP
CCP
PPC

4
PPPP
CYZY
CCPY
PPCC

5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
'''
# 브루트포스
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
import sys
input = sys.stdin.readline

N = int(input().rstrip())
candy = [list(str(input().rstrip())) for _ in range(N)]

