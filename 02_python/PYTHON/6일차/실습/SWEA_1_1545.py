# 1545.거꾸로 출력해 보아요
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T + 1):
    print(T-test_case,end = " ")