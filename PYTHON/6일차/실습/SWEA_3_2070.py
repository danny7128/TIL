# 2070.큰 놈, 작은 놈, 같은 놈
import sys
sys.stdin = open("input.txt", "r")

T = int(input())      

for test_case in range(1, T + 1):
    a ,b = map(int,input().split())
    print(f"#{test_case}",end=" ")
    if a < b:
        print('<')
    elif a == b:
        print('=')
    else:
        print('>')

