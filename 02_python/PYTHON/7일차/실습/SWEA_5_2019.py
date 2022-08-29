# 2019. 더블더블
import sys
sys.stdin = open("input.txt", "r")

a = 1
T = int(input())
for test_case in range(1, T + 2):
    print(a,end = " ")
    a *= 2

