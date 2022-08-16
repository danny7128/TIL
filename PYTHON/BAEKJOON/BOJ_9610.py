# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 
# 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

import sys

sys.stdin = open("BOJ_9610.txt")

n = int(input())

Q1 = Q2 = Q3 = Q4 = AXIS = 0

list_ = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1
    else:
        AXIS += 1

print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")
print(f"Q4: {Q4}")
print(f"AXIS: {AXIS}")
