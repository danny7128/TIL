# 1986. 지그재그 숫자
import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    result_sum = 0
    N = int(input())
    for i in range(1,N+1):
        if i % 2 == 1:
            result_sum += i
        else:
            result_sum += -i
    print(f"#{test_case} {result_sum}")
