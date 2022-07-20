# 1284. 수도 요금 경쟁
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int,input().split())
    a = W * P
    b = 0
    if W <= R:
        b = Q
    else:
        b = Q + (W-R) * S
    
    if a < b:
        print(f'#{test_case} {a}')
    else:
        print(f'#{test_case} {b}')



