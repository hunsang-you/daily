# 달팽이는 올라가고 싶다.
import math

A, B, V = map(int, input().split())         # A : 올라가는 거리, B : 내려오는 거리, V : 총 가야할 거리
                                            # 2 / 1 / 5
up = V - A                                  # 마지막 낮 빼고 올라가야할 거리  # 3

up_day = math.ceil(up / (A - B))                       # 마지막 날 빼고 올라갈 거리  / 하루마다 올라간 거리 #  3

tot_day = up_day + 1                                # 마지막 낮에 올라가야 하므로 +1


print(tot_day)