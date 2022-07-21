# 1976. 시각 덧셈
import sys
sys.stdin = open("input_SWEA_11_1976.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    b = 0
    c = 0
    for i in range(len(a)):
        if i %2 ==0:
            b += a[i]
            if b >12:
                b %= 12
        else:
            c += a[i]
            if c > 60:
                b += 1
                c %= 60
    print(f'#{test_case} {b} {c}')
