import sys

sys.stdin = open("test.txt")

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



    


