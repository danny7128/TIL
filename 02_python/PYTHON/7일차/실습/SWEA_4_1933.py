# 1933. 간단한 N 의 약수
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    if T % test_case == 0:
        print(test_case, end = ' ')
